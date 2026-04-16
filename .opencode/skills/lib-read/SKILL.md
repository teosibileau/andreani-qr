---
name: lib-read
description: "Decode and extract tracking numbers from Andreani QR code images using the andreani_qr Python library. Use when writing Python code that needs to read QR codes programmatically without subprocess calls."
---

# Andreani QR Read - Python Library Usage

Extract Andreani tracking numbers from QR code images using Python imports.

## Prerequisites

The andreani-qr package must be installed in the Python environment:

```bash
pip install git+https://github.com/teosibileau/andreani-qr.git
```

## Supported Image Formats

Any image format supported by PIL (Pillow): PNG, JPEG, BMP, GIF, TIFF, and others.

## Usage

### Basic Read

```python
from andreani_qr.qr import QR

qr = QR.from_file("360002431028980.png")
print(qr.code)  # "360002431028980"
```

### Verify a Generated QR (Round-Trip)

```python
from andreani_qr.qr import QR

# Encode
qr = QR("360002431028980")
img = qr.encode()
img.save("label.png")

# Read back and verify
decoded = QR.from_file("label.png")
assert decoded.code == "360002431028980"
```

### Batch Read

```python
from pathlib import Path
from andreani_qr.qr import QR, InvalidCodeError

image_dir = Path("./scanned-labels")

for image_path in image_dir.glob("*.png"):
    try:
        qr = QR.from_file(str(image_path))
        print(f"{image_path.name}: {qr.code}")
    except (InvalidCodeError, IndexError) as e:
        print(f"{image_path.name}: failed to decode - {e}")
```

## Error Handling

`QR.from_file` can raise:
- `InvalidCodeError` if the decoded data is not a valid Andreani code.
- `IndexError` if no QR code is found in the image.
- PIL errors if the image file is corrupted or unreadable.

```python
from andreani_qr.qr import QR, InvalidCodeError

try:
    qr = QR.from_file("image.png")
    print(qr.code)
except InvalidCodeError as e:
    print(f"Not a valid Andreani code: {e}")
except IndexError:
    print("No QR code found in the image")
except Exception as e:
    print(f"Could not read image: {e}")
```

## API Reference

### `QR.from_file(filepath: str) -> QR`

Class method. Opens the image at `filepath`, decodes the first QR code found, validates the data as an Andreani tracking code, and returns a `QR` instance.

- **filepath** - Path to the image file.
- **Returns** a `QR` instance whose `.code` attribute holds the tracking number.
- **Raises** `InvalidCodeError` if the decoded data fails validation, `IndexError` if no QR code is detected.

### `QR.code: str`

The 15-digit Andreani tracking number.

## When to Use This Skill

Use this skill instead of `cli-read` when:
- Writing Python scripts or applications that need to extract tracking numbers
- Building automated verification pipelines for printed QR labels
- Processing scanned images in bulk from Python
- You need the tracking number as a string for further processing in code
