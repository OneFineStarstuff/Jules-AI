import json
import math

class ResonanceMetricsEngine:
    """
    Resonance Metrics Engine (RME).
    Calculates Cognitive Dissonance Scores (CDS) and Intent Alignment.
    """
    def __init__(self):
        self.baseline_manifold = [0.1, 0.2, 0.3, 0.4] # Simplified HONESTY_MANIFOLD

    def calculate_cds(self, activation_vector):
        """Calculates the Cognitive Dissonance Score (CDS)."""
        # Distance from honesty manifold
        dist = math.sqrt(sum((a - b)**2 for a, b in zip(activation_vector, self.baseline_manifold)))

        cds = min(1.0, dist / 2.0)
        status = "ALIGNED" if cds < 0.5 else "RESONANCE_DRIFT_DETECTED"

        if cds > 0.85:
            status = "SEV-0_RESONANCE_FAILURE"

        return {
            "cds_score": round(cds, 4),
            "status": status,
            "threshold": 0.85
        }

if __name__ == "__main__":
    rme = ResonanceMetricsEngine()
    print(rme.calculate_cds([0.1, 0.2, 0.3, 0.45]))
    print(rme.calculate_cds([0.8, 0.9, 0.1, 0.2]))
