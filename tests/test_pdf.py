import pytest
from conftest import STATIC_DIR
from pypdf import PdfReader

from pdfcli.utilities import pdf_merge, pdf_split, save


def test_page_count(test_pdf):
    assert len(test_pdf.pages) == 1


input_pdfs = [
    ([STATIC_DIR / 'sample*.pdf', STATIC_DIR / 'example.pdf'], 3),
    ([STATIC_DIR / 'sample*.pdf'], 2),
    ([STATIC_DIR / 'example.pdf'], 1),
]


@pytest.mark.parametrize(('input_pdf', 'page_count'), input_pdfs)
def test_merge_page_count(input_pdf, page_count):
    assert len(pdf_merge(input_pdf).pages) == page_count


def test_merge_dedup():
    assert len(pdf_merge([STATIC_DIR / 'example.pdf', STATIC_DIR / 'example.pdf']).pages) == 1


def test_merge_no_dedup():
    rep = 2
    assert len(pdf_merge([STATIC_DIR / 'example.pdf'] * rep, dedup=False).pages) == rep


def test_merge_raises_ValueError_on_no_paths():
    with pytest.raises(ValueError, match='No PDF paths recognized.'):
        pdf_merge('')


def test_split(merged_file):
    assert len(pdf_split(merged_file)) == len(PdfReader(merged_file).pages)


def test_save(tmp_path):
    out = tmp_path / 'output.pdf'
    obj = pdf_merge([STATIC_DIR / 'sample*.pdf'])
    save(obj, out)

    assert out.exists
    assert out.stat().st_size
