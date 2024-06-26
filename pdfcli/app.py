from datetime import datetime
from pathlib import Path
from typing import Annotated, Optional

import typer
from pypdf import PdfWriter

from pdfcli.utilities import pdf_merge, pdf_split, save

date = str(datetime.now()).translate(str.maketrans(':- ', '___')).split('.')[0]
DEFAULT_PATH = Path.cwd()
DEFAULT_MERGE = DEFAULT_PATH / f'{date}_merged.pdf'

app = typer.Typer(rich_markup_mode='rich')


@app.command()
def merge(
    filenames: list[Path] = typer.Argument(  # noqa: B008
        help='Use if you have multiple path or glob with different paths.'
    ),
    output: Annotated[
        Path, typer.Option(help='The path to the output merged PDF file.')
    ] = DEFAULT_MERGE,
    *,
    dedup: Annotated[
        bool, typer.Option(help='Whether to remove duplicate pages from the merged PDF.')
    ] = True,
) -> None:
    """Merge multiple PDF files into a single PDF file."""
    filenames = filenames if filenames else []
    obj = pdf_merge(filenames, dedup=dedup)
    save(obj, output)


@app.command()
def split(
    filename: Annotated[Path, typer.Argument(help='The path to the input PDF file.')],
    name_suffix: Annotated[
        str, typer.Option(help='The suffix to be added to the name of each split file.')
    ] = 'page',
    output: Annotated[
        Optional[Path],
        typer.Option(help='The path to the directory where the split files will be saved.'),
    ] = None,
) -> None:
    """Split file in single pages, save each with unique name based on [code]name_suffix[/code]."""
    output = output if output else Path.cwd()
    objs = pdf_split(filename)
    for i, obj in enumerate(objs):
        writer = PdfWriter()

        writer.add_page(obj)
        save(writer, output=output / f'{i}:0{len(str(len(objs)))}_{name_suffix}.pdf')


if __name__ == '__main__':
    app()  # pragma: no cover
