# Incident Disclosure Toolkit

> Structures a disclosure response: computes **notification obligations + deadlines** from incident
> facts and renders advisory skeletons. The honest way to build authority — do disclosure well.
>
> Part of the **Technika11y** suite · *Root access for everyone.*

![status](https://img.shields.io/badge/status-pre--alpha-orange)
![license](https://img.shields.io/badge/license-Apache--2.0-blue)
![python](https://img.shields.io/badge/python-3.10%2B-informational)

> ⚠️ **Not legal advice.** This is a checklist/skeleton generator to help you *structure* a
> response quickly. Deadlines are simplified, representative versions of real regimes. Confirm the
> specifics with counsel for the jurisdictions actually involved.

---

## Status — read this first

**Pre-alpha (`v0.1.0a0`). Honest state of the code:**

| Capability | State |
|---|---|
| GDPR Art. 33 (72h authority) + Art. 34 (high-risk individuals) | ✅ works, tested |
| US state breach notification + AG-threshold notice | ✅ works, tested |
| Coordinated vulnerability disclosure (~90 day) timeline | ✅ works, tested |
| Concrete deadline dates from `discovered_date` | ✅ works, tested |
| Advisory skeleton renderer | ✅ works |
| Exhaustive per-state / per-country rules, CCPA specifics, sector rules (HIPAA/GLBA) | ❌ not built — [roadmap](#roadmap) |

The rules are representative, not exhaustive — that limit is stated on every run and in this table.

## Why it exists

Authority in security is earned by handling disclosure *well*, not by claiming seniority. When an
incident lands, the first hour is chaos; this turns a set of facts into a concrete, dated checklist
so the response is structured instead of improvised.

## Usage

```bash
PYTHONPATH=src python -m disclosure.cli obligations examples/incident.json
PYTHONPATH=src python -m disclosure.cli advisory examples/incident.json
```

```
[ ] supervisory authority (by 2026-07-04) — Notify the supervisory authority within 72 hours ...
[ ] affected individuals — Notify affected individuals without undue delay where the risk is high ...
[ ] affected residents (by 2026-07-31) — Notify affected residents; US state laws vary ...
[ ] state attorney(s) general (by 2026-07-31) — Many states require notice to the AG above a threshold ...
```

## Roadmap

- [ ] Per-state US rules + CCPA/CPRA specifics
- [ ] Sector regimes (HIPAA, GLBA, PCI-DSS reporting)
- [ ] Notification-letter templates per audience
- [ ] Machine-readable output + the shared Technika11y CI gate

## License

[Apache-2.0](LICENSE). See [`SECURITY.md`](SECURITY.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).
