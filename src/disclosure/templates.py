"""Render response documents from incident facts + computed obligations. Skeletons to fill in,
not finished legal text."""


def render_advisory(incident, obs):
    lines = []
    lines.append("SECURITY ADVISORY — DRAFT (not legal advice)")
    lines.append("=" * 44)
    lines.append(f"Type:        {incident.get('type', '?')}")
    lines.append(f"Discovered:  {incident.get('discovered_date', '?')}")
    lines.append(f"Affected:    {incident.get('affected_count', '?')}")
    lines.append("")
    lines.append("Summary:")
    lines.append(f"  {incident.get('summary', '<describe the incident>')}")
    lines.append("")
    lines.append("Notification obligations (confirm with counsel):")
    if not obs:
        lines.append("  (none triggered by the facts provided)")
    for o in obs:
        by = f" by {o['deadline_date']}" if o.get("deadline_date") else ""
        lines.append(f"  [ ] {o['notify']}{by} — {o['message']} ({o['authority']})")
    lines.append("")
    lines.append("Remediation: <steps taken and planned>")
    lines.append("Contact:     <security contact>")
    return "\n".join(lines) + "\n"
