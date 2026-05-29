"""CLI bridge for chat-driven workflows. Wraps career_ops.agent_ops.

Usage from Bash (the chat agent's natural habitat):

    # Read-only
    python scripts/agent_cli.py list --tier Hot --needs cv --limit 10
    python scripts/agent_cli.py show <job_id>

    # Mutations — payload comes from stdin (so quoting/escaping stays sane)
    echo '{"score":92,"reasoning":"...","skills_match":[...], ...}' \
        | python scripts/agent_cli.py score <job_id>
    cat cv.json | python scripts/agent_cli.py cv <job_id>
    cat cl.json | python scripts/agent_cli.py cl <job_id>
    cat deliv.json | python scripts/agent_cli.py deliverable <job_id> ecommerce_teardown
    cat form.json | python scripts/agent_cli.py form <job_id>
    cat msg.json | python scripts/agent_cli.py outreach <job_id> <contact_id> linkedin_connection
    cat contacts.json | python scripts/agent_cli.py contacts <job_id>

    # No-payload mutations
    python scripts/agent_cli.py status <job_id> "Applied"

All subcommands print a single JSON line to stdout with the result.
Exit code is 0 on success, 1 on error.
"""
from __future__ import annotations

import argparse
import json
import sys

from career_ops import agent_ops


def _read_stdin_json() -> dict:
    raw = sys.stdin.read()
    if not raw.strip():
        print(json.dumps({"ok": False, "error": "stdin is empty — pipe a JSON payload"}))
        sys.exit(1)
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        print(json.dumps({"ok": False, "error": f"invalid JSON on stdin: {exc}"}))
        sys.exit(1)


def _emit(result: dict) -> None:
    print(json.dumps(result, ensure_ascii=False))
    sys.exit(0 if result.get("ok", False) is not False else 1)


def main() -> None:
    p = argparse.ArgumentParser(prog="agent_cli")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="List jobs (filtered)")
    p_list.add_argument("--tier", default=None)
    p_list.add_argument("--status", default=None)
    p_list.add_argument("--needs", default=None,
                        choices=["cv", "contacts", "outreach", "form", "deliverable"])
    p_list.add_argument("--limit", type=int, default=50)

    p_show = sub.add_parser("show", help="Show one job's full record")
    p_show.add_argument("job_id")

    p_status = sub.add_parser("status", help="Update job status")
    p_status.add_argument("job_id")
    p_status.add_argument("new_status")

    p_score = sub.add_parser("score", help="Persist chat-reasoned analysis (payload on stdin)")
    p_score.add_argument("job_id")

    p_cv = sub.add_parser("cv", help="Generate adapted CV (payload on stdin)")
    p_cv.add_argument("job_id")

    p_cl = sub.add_parser("cl", help="Generate cover letter (payload on stdin)")
    p_cl.add_argument("job_id")
    p_cl.add_argument("--contact-name", default=None)

    p_del = sub.add_parser("deliverable", help="Generate deliverable (payload on stdin)")
    p_del.add_argument("job_id")
    p_del.add_argument("type", choices=["digital_audit", "ecommerce_teardown", "brand_analysis", "action_plan"])
    p_del.add_argument("--company-url", default=None)

    p_form = sub.add_parser("form", help="Generate form responses (payload on stdin)")
    p_form.add_argument("job_id")
    p_form.add_argument("--ats", default=None, help="ATS platform name")

    p_out = sub.add_parser("outreach", help="Persist outreach message for one contact (payload on stdin)")
    p_out.add_argument("job_id")
    p_out.add_argument("contact_id")
    p_out.add_argument("variant", choices=["email", "linkedin_connection", "linkedin_inmail"])

    p_con = sub.add_parser("contacts", help="Save contacts list (payload on stdin)")
    p_con.add_argument("job_id")

    args = p.parse_args()

    if args.cmd == "list":
        rows = agent_ops.list_jobs(
            tier=args.tier, status=args.status, needs=args.needs, limit=args.limit,
        )
        _emit({"ok": True, "count": len(rows), "jobs": rows})

    elif args.cmd == "show":
        job = agent_ops.show_job(args.job_id)
        if not job:
            _emit({"ok": False, "error": f"job not found: {args.job_id}"})
        _emit({"ok": True, "job": job})

    elif args.cmd == "status":
        _emit(agent_ops.set_status(args.job_id, args.new_status))

    elif args.cmd == "score":
        _emit(agent_ops.score_job(args.job_id, _read_stdin_json()))

    elif args.cmd == "cv":
        _emit(agent_ops.generate_cv(args.job_id, _read_stdin_json()))

    elif args.cmd == "cl":
        _emit(agent_ops.generate_cover_letter(args.job_id, _read_stdin_json(), contact_name=args.contact_name))

    elif args.cmd == "deliverable":
        _emit(agent_ops.generate_deliverable(args.job_id, _read_stdin_json(), deliverable_type=args.type, company_url=args.company_url))

    elif args.cmd == "form":
        _emit(agent_ops.generate_form_responses(args.job_id, _read_stdin_json(), ats_platform=args.ats))

    elif args.cmd == "outreach":
        _emit(agent_ops.generate_outreach_for_contact(args.job_id, args.contact_id, args.variant, _read_stdin_json()))

    elif args.cmd == "contacts":
        payload = _read_stdin_json()
        if not isinstance(payload, list):
            _emit({"ok": False, "error": "stdin must be a JSON array of contact objects"})
        _emit(agent_ops.save_contacts(args.job_id, payload))


if __name__ == "__main__":
    main()
