from src.settings import AppSettings
from src.writer.agent.contracts import NewsEditorAgent
from src.writer.agent.draft_agent import DraftNewsEditorAgent
from src.writer.agent.openai_agent import OpenAINewsEditorAgent


def create_news_editor_agent(settings: AppSettings) -> NewsEditorAgent:
    match settings.writer_agent:
        case "draft":
            return DraftNewsEditorAgent()
        case "openai":
            return OpenAINewsEditorAgent(
                api_key=settings.openai_api_key,
                model=settings.openai_model,
            )
        case unknown:
            raise ValueError(
                "Unsupported TODAYINTECH_WRITER_AGENT value: "
                f"{unknown}. Expected one of: draft, openai."
            )
