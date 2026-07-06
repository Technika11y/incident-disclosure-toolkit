"""Compute disclosure / notification obligations from incident facts.

This is a CHECKLIST generator to structure a response — **not legal advice**. The deadlines are
simplified, representative versions of real regimes; confirm specifics with counsel for the
jurisdictions actually involved. Pure functions over supplied dates, so results are deterministic
and unit-testable.
"""
from datetime import date, timedelta


def _ob(rule, deadline_days, notify, message, authority):
    return {
        "rule": rule,
        "deadline_days": deadline_days,
        "notify": notify,
        "message": message,
        "authority": authority,
    }


def obligations(incident):
    """Return the notification obligations triggered by the incident facts."""
    obs = []
    personal = incident.get("personal_data", False)
    juris = set(incident.get("jurisdictions", []))
    count = incident.get("affected_count", 0)
    high_risk = incident.get("high_risk", False)

    if personal and ("EU" in juris or "UK" in juris):
        obs.append(_ob("gdpr-authority", 3, "supervisory authority",
            "Notify the supervisory authority within 72 hours of becoming aware.",
            "GDPR Art. 33"))
        if high_risk:
            obs.append(_ob("gdpr-individuals", None, "affected individuals",
                "Notify affected individuals without undue delay where the risk is high.",
                "GDPR Art. 34"))

    if personal and "US" in juris:
        obs.append(_ob("us-state-breach", 30, "affected residents",
            "Notify affected residents; US state laws vary (often 'without unreasonable delay', "
            "some cap at 30-60 days). Confirm each affected state.",
            "US state breach-notification laws"))
        if count >= 500:
            obs.append(_ob("us-ag-notice", 30, "state attorney(s) general",
                "Many states require notice to the AG above a threshold (commonly 500 residents).",
                "US state breach-notification laws"))

    if incident.get("type") == "vulnerability":
        obs.append(_ob("coordinated-disclosure", 90, "reporter and public",
            "Coordinated disclosure: acknowledge the reporter, agree a timeline, publish by ~90 days.",
            "coordinated vulnerability disclosure norm"))

    return obs


def with_deadlines(incident, obs):
    """Attach concrete deadline dates using the incident's discovered_date (ISO yyyy-mm-dd)."""
    discovered = incident.get("discovered_date")
    out = []
    for o in obs:
        deadline = None
        if discovered and o.get("deadline_days") is not None:
            y, m, d = (int(x) for x in discovered.split("-"))
            deadline = (date(y, m, d) + timedelta(days=o["deadline_days"])).isoformat()
        out.append({**o, "deadline_date": deadline})
    return out
