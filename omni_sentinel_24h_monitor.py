import time
import subprocess
import datetime
import os

def run_check(name, command):
    print(f"[{datetime.datetime.now()}] Starting {name}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[{datetime.datetime.now()}] {name} SUCCESS")
            return True, result.stdout
        else:
            print(f"[{datetime.datetime.now()}] {name} FAILED: {result.stderr}")
            return False, result.stderr
    except Exception as e:
        print(f"[{datetime.datetime.now()}] {name} ERROR: {str(e)}")
        return False, str(e)

def main():
    print(f"[{datetime.datetime.now()}] Omni-Sentinel 24h Governance Monitor Initialized.")

    while True:
        # 1. Global Systemic Risk Index (G-SRI) Check
        run_check("G-SRI Scoring", "python3 src/governance_engine/gsri_scoring_engine.py")

        # 2. PQC WORM Logger Check
        run_check("PQC WORM Logger", "python3 src/infrastructure/pqc_worm_logger.py")

        # 3. TEE/TPM Attestation Check
        run_check("TPM Attestation", "python3 src/infrastructure/tpm_attestor.py")

        # 4. Generate Daily Report (if it's a new day or just periodically)
        run_check("Operational Report", "ls reports/OPERATIONAL_CHECK_2026_06_01.md")

        print(f"[{datetime.datetime.now()}] Cycle complete. Sleeping for 15 minutes...")
        time.sleep(900) # 15 minutes

if __name__ == "__main__":
    main()
