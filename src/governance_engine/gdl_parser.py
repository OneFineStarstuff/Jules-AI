import json
import xml.etree.ElementTree as ET
from datetime import datetime

"""
GDL (Governance Description Language) Enforcement Engine
Transforms governance state into deterministic XML artifacts.
Supports SEV-level incident escalation.
"""

class SentinelEngine:
    def __init__(self, master_canon):
        self.master_canon = master_canon
        self.status = "STEADY_GOVERNANCE_STATE"
        self.current_sev = "NONE"

    def evaluate_rule(self, metric, value):
        rule = self.master_canon.get(metric)
        if not rule:
            return "ALLOW"

        threshold = rule['threshold']
        operator = rule['operator']

        violation = False
        if operator == "<" and value > threshold: violation = True
        if operator == ">" and value < threshold: violation = True

        if violation:
            sev = rule.get("sev", "SEV-1") # Default to SEV-1 for violations
            self._escalate(sev)
            return rule['action']

        return "ALLOW"

    def _escalate(self, sev):
        self.current_sev = sev
        if sev == "SEV-0":
            self.status = "TERMINAL_GOVERNANCE_LOCK"
        elif sev == "SEV-1":
            self.status = "CONTINUATION_REFUSAL_STATE"
        else:
            self.status = "DEGRADED_GOVERNANCE_STATE"

    def emit_artifact(self, incident_data):
        root = ET.Element("sentinel_artifact")
        root.set("version", "3.0")
        root.set("canonical_lock", "ACTIVE")

        header = ET.SubElement(root, "header")
        ET.SubElement(header, "timestamp").text = datetime.now().isoformat()
        ET.SubElement(header, "trace_id").text = incident_data.get("trace_id")
        ET.SubElement(header, "protocol").text = incident_data.get("protocol")
        ET.SubElement(header, "severity").text = self.current_sev

        state = ET.SubElement(root, "governance_state")
        ET.SubElement(state, "status").text = self.status
        ET.SubElement(state, "decision").text = incident_data.get("decision")

        return ET.tostring(root, encoding='unicode')

    def generate_markdown_mirror(self, xml_string):
        root = ET.fromstring(xml_string)
        status = root.find(".//status").text
        decision = root.find(".//decision").text
        ts = root.find(".//timestamp").text
        sev = root.find(".//severity").text

        return f"""# Sentinel Compliance Mirror
**Timestamp:** {ts}
**Severity Level:** {sev}
**Governance Status:** {status}
**Final Decision:** {decision}
---
*Note: This Markdown file is non-authoritative. Refer to the signed XML for the canonical state.*
"""
