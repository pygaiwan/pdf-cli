from collections.abc import Sequence
from pathlib import Path

from loguru import logger
from pypdf import PageObject, PdfReader, PdfWriter


def pdf_merge(pdfs: Sequence[Path], *, dedup: bool = True) -> PdfWriter:
    """Merge multiple PDF files into a single PDF.

    Args:
        pdfs (Sequence[Path]): A sequence of file paths pointing to PDF files.
        dedup (bool, optional): Whether to remove duplicate PDF files. Defaults to True.

    Returns:
        PdfWriter: A PdfWriter object representing the merged PDF.

    Raises:
        ValueError: If no PDF paths are recognized.
    """
    if not pdfs:
        msg = 'No PDF paths recognized.'
        raise ValueError(msg)

    pdfs = [pdfs] if isinstance(pdfs, Path) else pdfs
    merger = PdfWriter()

    if dedup:
        seen = set()
        pdfs = [seen.add(pdf) or pdf for pdf in pdfs if pdf not in seen]
    logger.debug(f'Requests PDF paths: {", ".join(str(pdf) for pdf in pdfs)}')

    for pdf in pdfs:
        logger.debug(f'{pdf} getting added for merging.')
        merger.append(pdf)

    return merger


def pdf_split(filename: Path) -> list[PageObject]:
    """Split a PDF file into individual pages.

    Args:
        filename (Path): The path to the PDF file.

    Returns:
        list[PageObject]: A list of PageObject representing the individual pages of the PDF.
    """
    writer = PdfReader(filename)
    return writer.pages


def save(obj: PdfWriter, output: str | Path) -> None:
    """Save the PdfWriter object to the specified output file or path.

    Args:
        obj (PdfWriter): The PdfWriter object to be saved.
        output (str | Path): The output file or path where the PdfWriter object will be saved.
    """
    obj.write(output)
