import unittest

from disclosure.obligations import obligations, with_deadlines


def inc(**over):
    base = {
        "type": "breach", "personal_data": True, "jurisdictions": ["US", "EU"],
        "affected_count": 1200, "discovered_date": "2026-07-01", "high_risk": True,
    }
    base.update(over)
    return base


def rules(incident):
    return [o["rule"] for o in obligations(incident)]


class ObligationsTests(unittest.TestCase):
    def test_gdpr_authority_triggered(self):
        self.assertIn("gdpr-authority", rules(inc()))

    def test_gdpr_individuals_only_when_high_risk(self):
        self.assertIn("gdpr-individuals", rules(inc(high_risk=True)))
        self.assertNotIn("gdpr-individuals", rules(inc(high_risk=False)))

    def test_us_state_breach(self):
        self.assertIn("us-state-breach", rules(inc(jurisdictions=["US"])))

    def test_us_ag_notice_over_threshold(self):
        self.assertIn("us-ag-notice", rules(inc(jurisdictions=["US"], affected_count=500)))
        self.assertNotIn("us-ag-notice", rules(inc(jurisdictions=["US"], affected_count=100)))

    def test_vulnerability_triggers_coordinated_disclosure(self):
        self.assertIn("coordinated-disclosure",
                      rules(inc(type="vulnerability", personal_data=False, jurisdictions=[])))

    def test_no_obligations_when_nothing_triggers(self):
        self.assertEqual(obligations(inc(type="incident", personal_data=False, jurisdictions=[])), [])

    def test_deadline_date_is_computed_from_discovered_date(self):
        obs = with_deadlines(inc(jurisdictions=["EU"]), obligations(inc(jurisdictions=["EU"])))
        gdpr = next(o for o in obs if o["rule"] == "gdpr-authority")
        self.assertEqual(gdpr["deadline_date"], "2026-07-04")  # 2026-07-01 + 72h


if __name__ == "__main__":
    unittest.main()
