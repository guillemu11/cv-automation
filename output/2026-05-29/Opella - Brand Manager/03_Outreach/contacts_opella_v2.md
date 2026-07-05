# Opella outreach contacts — v2 expanded

**Job:** Brand Manager — Opella Dubai (posting pulled May 2026)
**Strategy shift:** speculative outreach to AMET org. Landings deployed at
[paula-pitch-a.vercel.app](https://paula-pitch-a.vercel.app) (Buscopan) and
[paula-pitch-b.vercel.app](https://paula-pitch-b.vercel.app) (Doliprane).
**Updated:** 2026-05-29.

> ⚠️ Email status
> Hunter.io key not configured → all emails are pattern-guesses
> (`firstname.lastname@opella.com`) with `status: unverified`. Opella's
> corporate domain is confirmed via ZoomInfo / RocketReach public listings.
> One outlier: **Amal Fathy** appeared as `@sanofi.com` on ZoomInfo because
> the Sanofi → Opella spin-off (Oct 2024) may not have fully migrated her
> Science Hub team yet. Both patterns listed for her.

## Contacts ranked by tier

### A-tier — Hiring Manager / decision-maker

| Person | Title | LinkedIn | Email (pattern) |
|---|---|---|---|
| **Murali Rao** ⭐ | Head of Brand & Innovation, AMET (Opella) | [linkedin](https://tr.linkedin.com/in/murali-rao) | `murali.rao@opella.com` |
| **Duygu Çetin** | Head of Brand & Innovation / Regional Marketing Director AMET (Opella) | [linkedin](https://www.linkedin.com/in/duygu-%C3%A7etin-abbbbb227/) | `duygu.cetin@opella.com` |

### B-tier — Country / Commercial sign-off

| Person | Title | LinkedIn | Email (pattern) |
|---|---|---|---|
| **Hossam Abo Ouf** ⭐ | Country Head, KSA & UAE (Opella) | [linkedin](https://sa.linkedin.com/in/hossam-abo-ouf-75102b11) | `hossam.ouf@opella.com` |
| **Pelit Duman** | Country GM Türkiye (Opella) | [linkedin](https://tr.linkedin.com/in/pelit-duman) | `pelit.duman@opella.com` |
| **Marianne Abou Elkheir** | Head Africa Middle Markets Partner (Opella, Paris) | [linkedin](https://www.linkedin.com/in/marianne-abou-elkheir-57826028) | `marianne.elkheir@opella.com` |

### C-tier — Peer Brand Managers (future colleagues)

| Person | Title | LinkedIn | Email (pattern) |
|---|---|---|---|
| **Olivia Stefanelli** | Senior Brand Manager (Opella, NY) — same role you want, different geo | [linkedin](https://www.linkedin.com/in/olivia-stefanelli-68369159/) | `olivia.stefanelli@opella.com` |
| **Sid Ali Bentarcha** | Opella (role TBD via LinkedIn login) | [linkedin](https://www.linkedin.com/in/sid-ali-bentarcha-628b1824/) | `sid.bentarcha@opella.com` |

### D-tier — Cross-functional peers

| Person | Title | LinkedIn | Email (pattern) |
|---|---|---|---|
| **Shahab Fraz Mirza** ⭐ | Trade & Revenue Mgmt Head AMET (Opella, UAE-based) | [linkedin](https://ae.linkedin.com/in/shahab-fraz-mirza) | `shahab.mirza@opella.com` |
| **Ahsan Rizvi** ⭐ | Digital Lead AMET (Opella) | [linkedin](https://www.linkedin.com/in/ahsanrizvi/) | `ahsan.rizvi@opella.com` |
| **Amal Fathy** | AMET Science Hub Head (Sanofi CHC / Opella, Cairo) | [linkedin](https://eg.linkedin.com/in/amal-fathy-5a621b140) | `amal.fathy@opella.com` *or* `amal.fathy@sanofi.com` |

### E-tier — Referral nodes / alumni

| Person | Title | LinkedIn | Email (pattern) |
|---|---|---|---|
| **Rashmi Gupta** | Ex–Head of Brand & Innovation AMET (Opella, now London) | [linkedin](https://www.linkedin.com/in/rashmi-gupta-674a283/) | `rashmi.gupta@opella.com` |
| **Ahmed El Kamhawy** | AMET Leadership Team (Opella, Egypt likely) | [linkedin](https://www.linkedin.com/in/ahmed-el-kamhawy-48b9a763/) | `ahmed.kamhawy@opella.com` |
| **Jamal Ali** | Opella (role TBD via LinkedIn login) | [linkedin](https://www.linkedin.com/in/jamal-ali-4b44b145/) | `jamal.ali@opella.com` |

## Recommended outreach order

Since the posting was pulled but the org structure is intact, the play is
speculative: 3-touch sequence per contact, 4–5 days apart, **non-overlapping
contacts on the same day** (so they don't compare notes and see a coordinated
wave).

| Week | Day 1 | Day 4 | Day 8 |
|---|---|---|---|
| 1 | **Murali Rao** — LinkedIn connection note → 4 days later InMail+landing | **Hossam Abo Ouf** — LinkedIn note → email follow-up | **Olivia Stefanelli** — peer-to-peer warm note |
| 2 | **Duygu Çetin** — InMail w/ landing | **Marianne Abou Elkheir** — Paris-side outreach | **Shahab Mirza** — UAE coffee request |
| 3 | **Ahsan Rizvi** — digital angle pitch | **Pelit Duman** — Turkey context | **Rashmi Gupta** — warm intro request to Murali |
| 4 (if quiet) | **Ahmed El Kamhawy** — AMET context | **Sid Ali Bentarcha** — connection | **Jamal Ali** — connection |

**A-tier first** (Murali, Duygu, Hossam) — they decide. C-tier (Olivia) is the
strongest peer-to-peer warm intro path. E-tier last as referral pressure if
the A-tier doesn't bite by week 3.

## Files on disk

- [`data/contacts/f324f5af0ff41e06.json`](data/contacts/f324f5af0ff41e06.json) — full Contact dataclass list (dashboard-compatible)
- [`data/contacts/f324f5af0ff41e06.emails.json`](data/contacts/f324f5af0ff41e06.emails.json) — per-contact email candidates + status + notes
- [`data/contacts/f324f5af0ff41e06.meta.json`](data/contacts/f324f5af0ff41e06.meta.json) — search metadata (v2 marker)

## If you add HUNTER_API_KEY later

Just run:

```
python scripts/_inject_opella_contacts_v2.py
```

The `email_finder.enrich_name` call inside picks up `settings.hunter_api_key`
automatically, runs `domain-search` once to detect Opella's dominant pattern,
then verifies each candidate. The `status` field flips from `unverified`
to `deliverable` / `risky` / `undeliverable` per email. No other changes
needed.
