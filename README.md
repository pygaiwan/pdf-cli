[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


Simple CMD tool for merging and splitting PDF files.

# Installation

```console
$ git clone https://github.com/pygaiwan/pdf-cli/
$ cd pdf-cli
$ pip install .
```

This will create a shell command `pdfcli` which will invoke the CLI app.

# Usage

## Split a PDF

```console
$ pdfcli split large_pdf.pdf
```

Optionally the options `name_suffix` and `output` can be specified. `name_suffix` specifies the end of the files produced which will then become: `0_<suffix>`, `1_<suffix>` etc.
`output` determines the path of the output, the default is the current working directory.


## Merge PDFs

```console
$ pdfcli merge /path/to/pdf1.pdf /path/to/pdf2.pdf /path/to/sample*.pdf
```

By default the dedupliation of files based on the same path is set to `True`. It can be switched off with `--no-dedup`.
Similarly to `split`, the `output` option can be set to define the path where the merged file will be created.

The expansion of characters like `*` is handled by bash. Not tested in Windows.