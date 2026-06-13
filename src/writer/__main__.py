import argparse
from pathlib import Path

from src.processing.article_candidate import PreprocessingResult
from src.processing.briefed_article_store import BriefedArticleStore
from src.settings import SETTINGS
from src.writer import DraftNewsEditorAgent, NewsWriter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.writer",
        description="Write Today in Tech Markdown documents from preprocessing output.",
    )
    parser.add_argument(
        "--date",
        help="Target date directory in YYYY-MM-DD format. Defaults to TODAYINTECH_TARGET_DATE or today.",
    )
    parser.add_argument(
        "--processed-dir",
        default=str(SETTINGS.processed_output_dir),
        help="Preprocessing output root. Defaults to TODAYINTECH_PROCESSED_OUTPUT_DIR.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(SETTINGS.output_dir),
        help="Markdown output root. Defaults to TODAYINTECH_OUTPUT_DIR or docs.",
    )
    parser.add_argument(
        "--briefed-state",
        default=str(SETTINGS.briefed_articles_path),
        help="Briefed articles state JSON path.",
    )
    return parser


def load_preprocessing_result(processed_date_dir: Path) -> PreprocessingResult:
    input_path = processed_date_dir / "preprocessing.json"
    if not input_path.exists():
        raise FileNotFoundError(f"Preprocessing result not found: {input_path}")
    return PreprocessingResult.model_validate_json(input_path.read_text(encoding="utf-8"))


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    target_date = SETTINGS.resolve_target_date(args.date)
    preprocessing_result = load_preprocessing_result(Path(args.processed_dir) / target_date)
    writer = NewsWriter(
        agent=DraftNewsEditorAgent(),
        output_dir=Path(args.output_dir),
        briefed_article_store=BriefedArticleStore(Path(args.briefed_state)),
    )
    result = writer.write(preprocessing_result)

    print("Writer results")
    print("==============")
    print(f"Generated for: {result.generated_for}")
    print(f"Written files: {len(result.written_paths)}")
    for path in result.written_paths:
        print(f"- {path}")


if __name__ == "__main__":
    main()
