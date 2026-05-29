"""키움증권 시세 API 메뉴."""

from pathlib import Path

from _doc_runtime import run_document_api_menu


_DOC_DIR = Path(__file__).resolve().parents[2] / "docs" / "키움 REST API 문서" / "mrkcond"


def run_mrkcond_api_menu(token: str):
    run_document_api_menu(
        token=token,
        title="시세",
        doc_dir=_DOC_DIR,
        default_url_path="/api/dostk/mrkcond",
        log_name="mrkcond",
    )
