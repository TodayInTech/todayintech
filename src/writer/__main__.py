import argparse
from pathlib import Path

from src.processing.article_candidate import PreprocessingResult
from src.processing.briefed_article_store import BriefedArticleStore
from src.progress import log_step
from src.settings import SETTINGS
from src.writer import NewsWriter
from src.writer.agent.factory import create_news_editor_agent


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
    parser.add_argument(
        "--agent",
        choices=["draft", "openai"],
        default=SETTINGS.writer_agent,
        help="Writer agent implementation. Defaults to TODAYINTECH_WRITER_AGENT or draft.",
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
    settings = SETTINGS
    if args.agent != SETTINGS.writer_agent:
        settings = SETTINGS.with_writer_agent(args.agent)

    log_step(1, 2, "Writer CLI", f"전처리 결과 로드 시작: date={target_date}")
    preprocessing_result = load_preprocessing_result(Path(args.processed_dir) / target_date)
    log_step(
        1,
        2,
        "Writer CLI",
        f"전처리 결과 로드 완료: candidates={preprocessing_result.candidate_count}",
    )
    writer = NewsWriter(
        agent=create_news_editor_agent(settings),
        output_dir=Path(args.output_dir),
        briefed_article_store=BriefedArticleStore(Path(args.briefed_state)),
    )
    log_step(2, 2, "Writer CLI", f"문서 작성 시작: agent={settings.writer_agent}")
    result = writer.write(preprocessing_result)
    log_step(2, 2, "Writer CLI", f"문서 작성 완료: files={len(result.written_paths)}")

    print("Writer results")
    print("==============")
    print(f"Generated for: {result.generated_for}")
    print(f"Written files: {len(result.written_paths)}")
    for path in result.written_paths:
        print(f"- {path}")


if __name__ == "__main__":
    main()
