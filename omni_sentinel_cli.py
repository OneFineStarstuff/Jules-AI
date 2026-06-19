import argparse
from omni_sentinel_24h_monitor import OmniSentinelMonitor


def main():
    parser = argparse.ArgumentParser(description="Omni-Sentinel CLI")
    parser.add_argument("--check", action="store_true", help="Run 24h governance check")
    args = parser.parse_args()

    if args.check:
        monitor = OmniSentinelMonitor()
        monitor.run_checks()


if __name__ == "__main__":
    main()
