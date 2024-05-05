from pathlib import Path

import pytest
from pypdf import PdfReader, PdfWriter

STATIC_DIR = Path(__file__).parent / 'static'


@pytest.fixture()
def test_pdf():
    writer = PdfWriter()
    writer.add_blank_page(width=595, height=842)
    writer.write(STATIC_DIR / 'example.pdf')
    return PdfReader(STATIC_DIR / 'example.pdf')


@pytest.fixture()
def output_file(tmp_path):
    out = tmp_path / 'out.pdf'
    return out.as_posix()


@pytest.fixture()
def merged_file():
    out = STATIC_DIR / 'merged.pdf'
    return out.as_posix()
