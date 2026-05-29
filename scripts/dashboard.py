#!/usr/bin/env python3
"""Local dashboard for reviewing scored jobs.

Serves a single-page app on localhost:8050 that shows all scored jobs
with the AI's analysis and lets you (and Paula) rate them manually.
Saves your ratings to data/golden_set.yaml for scorer calibration.

Usage:
    python scripts/dashboard.py
"""
import http.server
import json
import socketserver
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SCORED = DATA / "scored_jobs.json"
GOLDEN = DATA / "golden_set.yaml"
PORT = 8050


def load_scored() -> list[dict]:
    if not SCORED.exists():
        return []
    with SCORED.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_ratings() -> dict[str, dict]:
    if not GOLDEN.exists():
        return {}
    import yaml
    with GOLDEN.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []
    return {r["job_id"]: r for r in data if isinstance(r, dict)}


def save_rating(job_id: str, tier: str, user: str, reasoning: str, scored_jobs: list[dict]) -> None:
    import yaml
    existing = load_ratings()
    job = next((j for j in scored_jobs if j["id"] == job_id), None)
    if not job:
        return
    existing[job_id] = {
        "job_id": job_id,
        "title": job["title"],
        "company": job["company"],
        "location": job.get("location", ""),
        "source": job.get("source", ""),
        "tier": tier,
        "score": {"Hot": 90, "Warm": 70, "Cold": 40, "Reject": 10}.get(tier, 50),
        "reasoning": reasoning or f"Rated {tier} by {user}",
        "description_preview": job.get("description", "")[:500],
        "rated_by": user,
    }
    data = list(existing.values())
    GOLDEN.parent.mkdir(parents=True, exist_ok=True)
    with GOLDEN.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def build_html(scored_jobs: list[dict], ratings: dict[str, dict]) -> str:
    jobs_json = json.dumps(scored_jobs, ensure_ascii=False)
    ratings_json = json.dumps(ratings, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Career Ops Dashboard — Paula (Dubai)</title>
<style>
  :root {{
    --hot: #ef4444; --warm: #f59e0b; --cold: #3b82f6; --reject: #6b7280;
    --bg: #0f172a; --card: #1e293b; --card-hover: #334155;
    --text: #e2e8f0; --text-dim: #94a3b8; --border: #334155;
    --accent: #818cf8;
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ font-family: 'Segoe UI',system-ui,sans-serif; background:var(--bg); color:var(--text); }}

  .header {{
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border-bottom: 1px solid var(--border);
    padding: 20px 32px; display:flex; align-items:center; justify-content:space-between;
  }}
  .header h1 {{ font-size:22px; font-weight:600; }}
  .header h1 span {{ color: var(--accent); }}

  .stats {{ display:flex; gap:16px; }}
  .stat {{ text-align:center; padding:8px 16px; border-radius:8px; background:var(--card); }}
  .stat .num {{ font-size:24px; font-weight:700; }}
  .stat .label {{ font-size:11px; color:var(--text-dim); text-transform:uppercase; letter-spacing:1px; }}
  .stat.hot .num {{ color:var(--hot); }}
  .stat.warm .num {{ color:var(--warm); }}
  .stat.cold .num {{ color:var(--cold); }}

  .filters {{
    padding:12px 32px; display:flex; gap:8px; border-bottom:1px solid var(--border);
    background: var(--card); flex-wrap: wrap; align-items: center;
  }}
  .filters label {{ font-size:12px; color:var(--text-dim); margin-right:4px; }}
  .filter-btn {{
    padding:6px 14px; border-radius:16px; border:1px solid var(--border);
    background:transparent; color:var(--text); cursor:pointer; font-size:13px;
    transition: all 0.15s;
  }}
  .filter-btn:hover {{ background:var(--card-hover); }}
  .filter-btn.active {{ background:var(--accent); border-color:var(--accent); color:#fff; }}

  .grid {{
    display:grid; grid-template-columns: repeat(auto-fill, minmax(420px,1fr));
    gap:16px; padding:24px 32px;
  }}

  .card {{
    background:var(--card); border-radius:12px; border:1px solid var(--border);
    overflow:hidden; transition: transform 0.15s, box-shadow 0.15s;
  }}
  .card:hover {{ transform:translateY(-2px); box-shadow:0 8px 24px rgba(0,0,0,0.3); }}

  .card-header {{
    padding:16px 20px 12px; display:flex; justify-content:space-between; align-items:flex-start;
  }}
  .card-header .title {{ font-size:15px; font-weight:600; line-height:1.3; flex:1; }}
  .card-header .company {{ font-size:13px; color:var(--text-dim); margin-top:3px; }}

  .score-badge {{
    min-width:52px; height:52px; border-radius:12px; display:flex; flex-direction:column;
    align-items:center; justify-content:center; font-weight:700; font-size:18px;
    margin-left:12px; flex-shrink:0;
  }}
  .score-badge .tier-label {{ font-size:9px; text-transform:uppercase; letter-spacing:1px; opacity:0.8; }}
  .score-badge.hot {{ background:rgba(239,68,68,0.15); color:var(--hot); border:1px solid rgba(239,68,68,0.3); }}
  .score-badge.warm {{ background:rgba(245,158,11,0.15); color:var(--warm); border:1px solid rgba(245,158,11,0.3); }}
  .score-badge.cold {{ background:rgba(59,130,246,0.15); color:var(--cold); border:1px solid rgba(59,130,246,0.3); }}

  .card-meta {{
    padding:0 20px 12px; display:flex; gap:8px; flex-wrap:wrap;
  }}
  .tag {{
    font-size:11px; padding:3px 8px; border-radius:4px;
    background:rgba(255,255,255,0.06); color:var(--text-dim);
  }}
  .tag.sector {{ border-left:2px solid var(--accent); }}
  .tag.seniority {{ border-left:2px solid #10b981; }}

  .reasoning {{
    padding:0 20px 12px; font-size:13px; color:var(--text-dim); line-height:1.5;
  }}

  .details {{ padding:0 20px 12px; }}
  .detail-toggle {{
    font-size:12px; color:var(--accent); cursor:pointer; background:none; border:none;
    padding:4px 0;
  }}
  .detail-content {{
    display:none; padding:10px 0; font-size:12px; line-height:1.6;
  }}
  .detail-content.open {{ display:block; }}
  .detail-content .label {{ color:var(--text-dim); font-weight:600; }}
  .skills {{ display:flex; flex-wrap:wrap; gap:4px; margin-top:4px; }}
  .skill {{ padding:2px 8px; border-radius:3px; font-size:11px; }}
  .skill.match {{ background:rgba(16,185,129,0.15); color:#10b981; }}
  .skill.missing {{ background:rgba(239,68,68,0.1); color:#f87171; }}
  .skill.ats {{ background:rgba(129,140,248,0.15); color:var(--accent); }}
  .red-flag {{ color:#f87171; margin:2px 0; }}

  .card-footer {{
    padding:12px 20px; border-top:1px solid var(--border);
    display:flex; align-items:center; justify-content:space-between;
  }}
  .rate-section {{ display:flex; gap:6px; align-items:center; }}
  .rate-section label {{ font-size:11px; color:var(--text-dim); }}
  .rate-btn {{
    width:32px; height:32px; border-radius:8px; border:1px solid var(--border);
    cursor:pointer; font-size:12px; font-weight:600; display:flex;
    align-items:center; justify-content:center; transition:all 0.15s;
    background:transparent;
  }}
  .rate-btn:hover {{ transform:scale(1.1); }}
  .rate-btn.h {{ color:var(--hot); }} .rate-btn.h:hover,.rate-btn.h.selected {{ background:var(--hot); color:#fff; }}
  .rate-btn.w {{ color:var(--warm); }} .rate-btn.w:hover,.rate-btn.w.selected {{ background:var(--warm); color:#fff; }}
  .rate-btn.c {{ color:var(--cold); }} .rate-btn.c:hover,.rate-btn.c.selected {{ background:var(--cold); color:#fff; }}
  .rate-btn.r {{ color:var(--reject); }} .rate-btn.r:hover,.rate-btn.r.selected {{ background:var(--reject); color:#fff; }}

  .rated-indicator {{ font-size:11px; padding:4px 10px; border-radius:4px; }}
  .rated-indicator.guille {{ background:rgba(129,140,248,0.15); color:var(--accent); }}
  .rated-indicator.paula {{ background:rgba(16,185,129,0.15); color:#10b981; }}

  .apply-link {{
    font-size:12px; color:var(--accent); text-decoration:none;
    padding:6px 12px; border:1px solid var(--accent); border-radius:6px;
    transition: all 0.15s;
  }}
  .apply-link:hover {{ background:var(--accent); color:#fff; }}

  .desc-preview {{
    padding: 0 20px 12px; max-height:0; overflow:hidden; transition: max-height 0.3s;
    font-size:12px; color:var(--text-dim); line-height:1.5;
  }}
  .desc-preview.open {{ max-height: 400px; overflow-y:auto; }}

  .empty {{ text-align:center; padding:60px; color:var(--text-dim); }}
  .user-select {{ padding:4px 8px; border-radius:4px; background:var(--card); color:var(--text); border:1px solid var(--border); font-size:13px; }}
</style>
</head>
<body>

<div class="header">
  <div>
    <h1><span>Career Ops</span> Dashboard</h1>
    <div style="font-size:12px;color:var(--text-dim);margin-top:4px;">Paula De Francisco — Brand & Marketing — Dubai</div>
  </div>
  <div class="stats" id="stats"></div>
</div>

<div class="filters">
  <label>Filter:</label>
  <button class="filter-btn active" onclick="setFilter('all')">All</button>
  <button class="filter-btn" onclick="setFilter('Hot')">Hot</button>
  <button class="filter-btn" onclick="setFilter('Warm')">Warm</button>
  <button class="filter-btn" onclick="setFilter('Cold')">Cold</button>
  <button class="filter-btn" onclick="setFilter('unrated')">Unrated</button>
  <span style="flex:1"></span>
  <label>Rater:</label>
  <select class="user-select" id="raterSelect">
    <option value="Guille">Guille</option>
    <option value="Paula">Paula</option>
  </select>
  <label style="margin-left:12px">Sort:</label>
  <select class="user-select" id="sortSelect" onchange="renderCards()">
    <option value="score-desc">Score (high first)</option>
    <option value="score-asc">Score (low first)</option>
    <option value="company">Company A-Z</option>
  </select>
</div>

<div class="grid" id="grid"></div>

<script>
const JOBS = {jobs_json};
const RATINGS = {ratings_json};
let currentFilter = 'all';
let localRatings = {{}};

// Load saved local ratings from localStorage
try {{
  localRatings = JSON.parse(localStorage.getItem('careerops_ratings') || '{{}}');
}} catch(e) {{}}

function saveLocalRating(jobId, tier, user) {{
  if (!localRatings[jobId]) localRatings[jobId] = {{}};
  localRatings[jobId][user] = tier;
  localStorage.setItem('careerops_ratings', JSON.stringify(localRatings));

  // Also POST to server to save to golden_set.yaml
  fetch('/rate', {{
    method: 'POST',
    headers: {{'Content-Type':'application/x-www-form-urlencoded'}},
    body: `job_id=${{encodeURIComponent(jobId)}}&tier=${{encodeURIComponent(tier)}}&user=${{encodeURIComponent(user)}}`
  }});
}}

function setFilter(f) {{
  currentFilter = f;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  event.target.classList.add('active');
  renderCards();
}}

function toggleDetail(id) {{
  document.getElementById('detail-'+id).classList.toggle('open');
}}
function toggleDesc(id) {{
  document.getElementById('desc-'+id).classList.toggle('open');
}}

function renderCards() {{
  const grid = document.getElementById('grid');
  const sort = document.getElementById('sortSelect').value;
  let jobs = [...JOBS];

  // Filter
  if (currentFilter === 'unrated') {{
    jobs = jobs.filter(j => !localRatings[j.id]);
  }} else if (currentFilter !== 'all') {{
    jobs = jobs.filter(j => j.ai_tier === currentFilter);
  }}

  // Sort
  if (sort === 'score-desc') jobs.sort((a,b) => b.ai_score - a.ai_score);
  else if (sort === 'score-asc') jobs.sort((a,b) => a.ai_score - b.ai_score);
  else if (sort === 'company') jobs.sort((a,b) => a.company.localeCompare(b.company));

  if (!jobs.length) {{
    grid.innerHTML = '<div class="empty">No jobs match this filter.</div>';
    return;
  }}

  grid.innerHTML = jobs.map(j => {{
    const tierClass = j.ai_tier.toLowerCase();
    const lr = localRatings[j.id] || {{}};
    const guilleRating = lr['Guille'] || '';
    const paulaRating = lr['Paula'] || '';

    const skillsHtml = (j.skills_match||[]).map(s => `<span class="skill match">${{s}}</span>`).join('');
    const missingHtml = (j.missing_skills||[]).map(s => `<span class="skill missing">${{s}}</span>`).join('');
    const atsHtml = (j.ats_keywords||[]).map(s => `<span class="skill ats">${{s}}</span>`).join('');
    const flagsHtml = (j.red_flags||[]).map(f => `<div class="red-flag">&#9888; ${{f}}</div>`).join('');

    const ratedIndicators = [
      guilleRating ? `<span class="rated-indicator guille">G: ${{guilleRating}}</span>` : '',
      paulaRating ? `<span class="rated-indicator paula">P: ${{paulaRating}}</span>` : '',
    ].filter(Boolean).join(' ');

    return `
      <div class="card">
        <div class="card-header">
          <div>
            <div class="title">${{j.title}}</div>
            <div class="company">${{j.company}} &middot; ${{j.location}}</div>
          </div>
          <div class="score-badge ${{tierClass}}">
            ${{j.ai_score}}
            <span class="tier-label">${{j.ai_tier}}</span>
          </div>
        </div>
        <div class="card-meta">
          <span class="tag">${{j.source}}</span>
          <span class="tag sector">${{j.sector_fit || 'N/A'}}</span>
          <span class="tag seniority">${{j.seniority_fit || 'N/A'}}</span>
          ${{j.salary_raw ? `<span class="tag">${{j.salary_raw}}</span>` : ''}}
        </div>
        <div class="reasoning">${{j.reasoning}}</div>
        <div class="details">
          <button class="detail-toggle" onclick="toggleDetail('${{j.id}}')">Skills & Details &#9662;</button>
          <div class="detail-content" id="detail-${{j.id}}">
            ${{skillsHtml ? `<div><span class="label">Matching skills:</span><div class="skills">${{skillsHtml}}</div></div>` : ''}}
            ${{missingHtml ? `<div style="margin-top:8px"><span class="label">Missing:</span><div class="skills">${{missingHtml}}</div></div>` : ''}}
            ${{atsHtml ? `<div style="margin-top:8px"><span class="label">ATS keywords to add to CV:</span><div class="skills">${{atsHtml}}</div></div>` : ''}}
            ${{flagsHtml ? `<div style="margin-top:8px"><span class="label">Red flags:</span>${{flagsHtml}}</div>` : ''}}
          </div>
          <button class="detail-toggle" onclick="toggleDesc('${{j.id}}')">Job Description &#9662;</button>
          <div class="desc-preview" id="desc-${{j.id}}">${{(j.description||'').replace(/\\n/g,'<br>')}}</div>
        </div>
        <div class="card-footer">
          <div class="rate-section">
            <label>Rate:</label>
            <button class="rate-btn h ${{getUserRating(j.id)==='Hot'?'selected':''}}" onclick="rate('${{j.id}}','Hot')" title="Hot">H</button>
            <button class="rate-btn w ${{getUserRating(j.id)==='Warm'?'selected':''}}" onclick="rate('${{j.id}}','Warm')" title="Warm">W</button>
            <button class="rate-btn c ${{getUserRating(j.id)==='Cold'?'selected':''}}" onclick="rate('${{j.id}}','Cold')" title="Cold">C</button>
            <button class="rate-btn r ${{getUserRating(j.id)==='Reject'?'selected':''}}" onclick="rate('${{j.id}}','Reject')" title="Reject">R</button>
            ${{ratedIndicators}}
          </div>
          ${{j.url ? `<a class="apply-link" href="${{j.url}}" target="_blank">View Job &#8599;</a>` : ''}}
        </div>
      </div>
    `;
  }}).join('');

  // Update stats
  const hot = JOBS.filter(j=>j.ai_tier==='Hot').length;
  const warm = JOBS.filter(j=>j.ai_tier==='Warm').length;
  const cold = JOBS.filter(j=>j.ai_tier==='Cold').length;
  const rated = Object.keys(localRatings).length;
  document.getElementById('stats').innerHTML = `
    <div class="stat hot"><div class="num">${{hot}}</div><div class="label">Hot</div></div>
    <div class="stat warm"><div class="num">${{warm}}</div><div class="label">Warm</div></div>
    <div class="stat cold"><div class="num">${{cold}}</div><div class="label">Cold</div></div>
    <div class="stat"><div class="num">${{rated}}/${{JOBS.length}}</div><div class="label">Rated</div></div>
  `;
}}

function getUserRating(jobId) {{
  const user = document.getElementById('raterSelect').value;
  return (localRatings[jobId]||{{}})[user] || '';
}}

function rate(jobId, tier) {{
  const user = document.getElementById('raterSelect').value;
  saveLocalRating(jobId, tier, user);
  renderCards();
}}

renderCards();
</script>
</body>
</html>"""


class DashboardHandler(http.server.BaseHTTPRequestHandler):
    scored_jobs = []

    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            ratings = load_ratings()
            html = build_html(self.scored_jobs, ratings)
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/rate":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            params = urllib.parse.parse_qs(body)
            job_id = params.get("job_id", [""])[0]
            tier = params.get("tier", [""])[0]
            user = params.get("user", ["Guille"])[0]
            if job_id and tier:
                save_rating(job_id, tier, user, f"Rated {tier} by {user}", self.scored_jobs)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, fmt, *args):
        pass  # silence request logs


def main():
    scored = load_scored()
    if not scored:
        print("No scored jobs found. Run the pipeline first.")
        sys.exit(1)

    DashboardHandler.scored_jobs = scored
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        print(f"\n  Career Ops Dashboard")
        print(f"  ====================")
        print(f"  {len(scored)} scored jobs loaded")
        print(f"  Open: http://localhost:{PORT}")
        print(f"  Press Ctrl+C to stop\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  Dashboard stopped.")


if __name__ == "__main__":
    main()
