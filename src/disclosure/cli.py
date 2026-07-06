"""incident-disclosure <obligations|advisory> <incident.json> — structure a disclosure response.

Not legal advice; a checklist/skeleton generator."""
import argparse
import json
import sys

from .obligations import obligations, with_deadlines
from .templates import render_advisory


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(prog="incident-disclosure")
    parser.add_argument("command", choices=["obligations", "advisory"])
    parser.add_argument("incident", help="incident facts JSON")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    with open(args.incident) as fh:
        incident = json.load(fh)
    obs = with_deadlines(incident, obligations(incident))

    if args.command == "obligations":
        if args.json:
            print(json.dumps(obs, indent=2))
        else:
            if not obs:
                print("no notification obligations triggered by the facts provided", file=sys.stderr)
            for o in obs:
                by = f" (by {o['deadline_date']})" if o.get("deadline_date") else ""
                print(f"[ ] {o['notify']}{by} — {o['message']}", file=sys.stderr)
        return 0

    # advisory
    print(render_advisory(incident, obs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
