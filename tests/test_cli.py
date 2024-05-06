from pathlib import Path

from conftest import STATIC_DIR
from typer.testing import CliRunner

from pdfcli.app import app

runner = CliRunner()


def test_merge_file_single_input(output_file):
    result = runner.invoke(
        app, ['merge', (STATIC_DIR / 'example.pdf').as_posix(), '--output', output_file]
    )
    assert result.exit_code == 0
    assert Path(output_file).exists
    assert Path(output_file).stat().st_size


def test_merge_file_multiple_input(output_file):
    in1 = (STATIC_DIR / 'example.pdf').as_posix()
    in2 = (STATIC_DIR / 'sample_1.pdf').as_posix()
    in3 = (STATIC_DIR / 'sample_2.pdf').as_posix()
    result = runner.invoke(app, ['merge', in1, in2, in3, '--output', output_file])
    assert result.exit_code == 0
    assert Path(output_file).exists
    assert Path(output_file).stat().st_size


def test_split_file(merged_file, tmp_path):
    result = runner.invoke(
        app, ['split', merged_file, '--output', tmp_path, '--name-suffix', 'page']
    )

    assert result.exit_code == 0
    assert len(list(Path(tmp_path).glob('*.pdf'))) == 2  # noqa: PLR2004
