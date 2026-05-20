"""키움증권 테마 API 메뉴."""

from pathlib import Path

from _doc_runtime import run_document_api_menu


_DOC_DIR = Path(__file__).resolve().parents[2] / "docs" / "키움 REST API 문서" / "thme"


def run_thme_api_menu(token: str):
    run_document_api_menu(
        token=token,
        title="테마",
        doc_dir=_DOC_DIR,
        default_url_path="/api/dostk/thme",
        log_name="thme",
    )
