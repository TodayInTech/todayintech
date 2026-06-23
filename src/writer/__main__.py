import argparse
from pathlib import Path

from src.enrichment.models import EnrichmentResult
from src.processing.state.briefed_article_store import BriefedArticleStore
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
        "--enriched-dir",
        default=str(SETTINGS.enriched_output_dir),
        help="Enrichment output root. Defaults to TODAYINTECH_ENRICHED_OUTPUT_DIR.",
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
    parser.add_argument(
        "--trace-dir",
        help="Optional trace output root. When set, writes writer decision trace JSON and Markdown.",
    )
    return parser


def load_enrichment_result(enriched_date_dir: Path) -> EnrichmentResult:
    input_path = enriched_date_dir / "enrichment.json"
    if not input_path.exists():
        raise FileNotFoundError(f"Enrichment result not found: {input_path}")
    return EnrichmentResult.model_validate_json(input_path.read_text(encoding="utf-8"))


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    target_date = SETTINGS.resolve_target_date(args.date)
    settings = SETTINGS
    if args.agent != SETTINGS.writer_agent:
        settings = SETTINGS.with_writer_agent(args.agent)

    log_step(1, 2, "Writer CLI", f"enrichment 결과 로드 시작: date={target_date}")
    enrichment_result = load_enrichment_result(Path(args.enriched_dir) / target_date)
    log_step(
        1,
        2,
        "Writer CLI",
        f"enrichment 결과 로드 완료: candidates={len(enrichment_result.candidates)}",
    )
    writer = NewsWriter(
        agent=create_news_editor_agent(settings),
        output_dir=Path(args.output_dir),
        briefed_article_store=BriefedArticleStore(Path(args.briefed_state)),
        trace_output_dir=Path(args.trace_dir) if args.trace_dir else None,
        agent_name=settings.writer_agent,
    )
    log_step(2, 2, "Writer CLI", f"문서 작성 시작: agent={settings.writer_agent}")
    result = writer.write(enrichment_result)
    log_step(2, 2, "Writer CLI", f"문서 작성 완료: files={len(result.written_paths)}")

    print("Writer results")
    print("==============")
    print(f"Generated for: {result.generated_for}")
    print(f"Written files: {len(result.written_paths)}")
    for path in result.written_paths:
        print(f"- {path}")
    if result.trace_paths:
        print(f"Trace files: {len(result.trace_paths)}")
        for path in result.trace_paths:
            print(f"- {path}")


if __name__ == "__main__":
    main()
