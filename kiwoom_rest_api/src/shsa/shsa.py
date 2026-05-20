"""키움증권 공매도 API 메뉴."""

from pathlib import Path

from _doc_runtime import run_document_api_menu


_DOC_DIR = Path(__file__).resolve().parents[2] / "docs" / "키움 REST API 문서" / "shsa"


def run_shsa_api_menu(token: str):
    run_document_api_menu(
        token=token,
        title="공매도",
        doc_dir=_DOC_DIR,
        default_url_path="/api/dostk/shsa",
        log_name="shsa",
    )
