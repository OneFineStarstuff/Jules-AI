import unittest
import os
import json

class TestGovernanceArtifacts(unittest.TestCase):
    def test_solidity_omega_actual_exists(self):
        self.assertTrue(os.path.exists("src/governance_engine/contracts/OmegaActual.sol"))

    def test_solidity_omni_sentinel_exists(self):
        self.assertTrue(os.path.exists("src/governance_engine/contracts/OmniSentinel.sol"))

    def test_oscal_catalog_valid_json(self):
        with open("regulator_submission_pack/OSCAL_GSIFI_CATALOG_V8.json", "r") as f:
            data = json.load(f)
            self.assertEqual(data["catalog"]["metadata"]["oscal-version"], "1.1.2")
            self.assertEqual(data["catalog"]["metadata"]["title"], "G-SIFI AGI/ASI Governance Control Catalog v8.0")

    def test_terraform_file_exists(self):
        self.assertTrue(os.path.exists("infrastructure/terraform/confidential_enclaves.tf"))
        with open("infrastructure/terraform/confidential_enclaves.tf", "r") as f:
            content = f.read()
            self.assertIn("aws_instance", content)
            self.assertIn("azurerm_linux_virtual_machine", content)

    def test_rego_policy_exists(self):
        self.assertTrue(os.path.exists("src/infrastructure/policies/compliance_rules.rego"))
        with open("src/infrastructure/policies/compliance_rules.rego", "r") as f:
            content = f.read()
            self.assertIn("package sentinel.compliance", content)
            self.assertIn("dora_compliant", content)

    def test_dashboard_exists(self):
        self.assertTrue(os.path.exists("src/adaptive-ui/GovernanceDashboard.tsx"))
        with open("src/adaptive-ui/GovernanceDashboard.tsx", "r") as f:
            content = f.read()
            self.assertIn("export const GovernanceDashboard", content)
            self.assertIn("G-SRI", content)

if __name__ == "__main__":
    unittest.main()
