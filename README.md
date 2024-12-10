# Andreani QR

## Setup

```
poetry install
```

## Usage

```
poetry run python andreani_qr/main.py
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Andreani QR tools.

Options:
  --help  Show this message and exit.

Commands:
  encode  Encodes the provided TEXT into a QR code and saves it as an...
  read    Reads the QR code from the provided image file.
```

### Encode code

```
poetry run python andreani_qr/main.py encode 360002431028980
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO Init
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO Processing 360002431028980
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO Instantiating QR code with version:1 error_correction:1 box_size:21 border:4
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO Adding data to QR
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO Generating QR code with fill: black and back:white
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO Saving QR code to ./360002431028980.png
2024-12-10 19:02:14 Teofilos-Air.localdomain andreani_qr[67683] INFO QR code generated and saved to ./360002431028980.png
```

### Read code from QR (debug)

```
poetry run python andreani_qr/main.py read ~/Downloads/code.jpeg
2024-12-08 11:00:50 Teofilos-Air.home andreani_qr[6948] INFO Init
2024-12-08 11:00:50 Teofilos-Air.home andreani_qr[6948] INFO Type: QRCODE, Data: 360002425903320
```
