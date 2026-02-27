# Andreani QR

## Setup

### Install

Install using pipx directly from the git repository:

```bash
pipx install git+https://github.com/teosibileau/andreani-qr.git
```

### Development

For local development, install dependencies with:

```bash
pipx install poetry
poetry install
```

## Usage

```
andreani-qr --help
Usage: andreani-qr [OPTIONS] COMMAND [ARGS]...

  Andreani QR tools.

Options:
  --help  Show this message and exit.

Commands:
  encode  Encode provided TEXT into a QR and save it as an image file.
  read    Read QR code from the provided image file.
```

### Encode code

```
andreani-qr encode 360002431028980
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO QR code generated and saved to ./360002431028980.png
```

You can also specify a custom filename with `-n` or `--name`:

```
andreani-qr encode 360002431028980 -n my-custom-name
```

### Read code from QR (debug)

```
andreani-qr read ~/Downloads/code.jpeg
2024-12-08 11:00:50 Teofilos-Air.home andreani_qr[6948] INFO Type: QRCODE, Data: 360002425903320
```
