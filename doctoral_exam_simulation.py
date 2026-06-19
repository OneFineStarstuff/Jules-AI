import time


class DoctoralSimulation:
    """Simulates the final doctoral exam for Sentinel AI architects."""
    def __init__(self):
        self.phase = "PREPARATION"

    def start_exam(self):
        self.phase = "EXAMINATION"
        time.sleep(1)
        return "SUCCESS"


if __name__ == "__main__":
    sim = DoctoralSimulation()
    sim.start_exam()
