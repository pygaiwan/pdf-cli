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

There are two ways to merge multiple PDFs. Via the argument `filenames`:

```console
$ pdfcli merge /path/to/pdf1.pdf /path/to/pdf2.pdf
```

Or via the `--expr` option, which resolve shell globbing.

```console
$ pdfcli merge --expr /path/to/pdf*.pdf 
```

Or a combination of both. By default the dedupliation of files based on the same path is set to `True`. It can be switched off with `--no-dedup`.
Similarly to `split`, the `output` option can be set to define the path where the merged file will be created.
