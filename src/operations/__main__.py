import argparse
from pathlib import Path

from src.operations.operations_data_writer import write_operations_data
from src.operations.trace_metrics_builder import build_trace_metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.operations",
        description="Build static Operations dashboard data from remote trace history.",
    )
    parser.add_argument(
        "--trace-history-dir",
        required=True,
        help="Checkout path for the remote tracing-history branch.",
    )
    parser.add_argument(
        "--output-dir",
        default="static/data/operations",
        help="Output directory for generated Operations JSON.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    metrics = build_trace_metrics(Path(args.trace_history_dir))
    written_path = write_operations_data(Path(args.output_dir), metrics)
    print("Operations dashboard data")
    print("=========================")
    print(f"Trace history: {args.trace_history_dir}")
    print(f"Runs: {len(metrics['runs'])}")
    print(f"Services: {len(metrics['services'])}")
    print(f"- {written_path}")


if __name__ == "__main__":
    main()
