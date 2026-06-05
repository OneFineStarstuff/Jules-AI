import json

class RedDawnContagionMatrix:
    """
    Red Dawn Stage 6: Cross-Border Sovereign Interoperability Stress Matrix.
    Maps failure modes to regulatory jurisdictions.
    """
    def __init__(self):
        self.matrix = {
            "US_Treasury": {"impact": "HIGH", "fail_mode": "Latency in PQC rotation"},
            "EU_ECB": {"impact": "CRITICAL", "fail_mode": "Semantic drift in Annex IV tags"},
            "MAS_Singapore": {"impact": "MEDIUM", "fail_mode": "Breach signature gossip delay"}
        }

    def get_stress_matrix(self):
        return self.matrix

if __name__ == "__main__":
    matrix = RedDawnContagionMatrix()
    print(json.dumps(matrix.get_stress_matrix(), indent=2))
