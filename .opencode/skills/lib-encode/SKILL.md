---
name: lib-encode
description: "Generate QR code images from Andreani tracking numbers using the andreani_qr Python library. Use when writing Python code that needs to create QR codes programmatically without subprocess calls."
---

# Andreani QR Encode - Python Library Usage

Generate QR code images from valid Andreani tracking numbers using Python imports.

## Prerequisites

The andreani-qr package must be installed in the Python environment:

```bash
pip install git+https://github.com/teosibileau/andreani-qr.git
```

## Valid Code Format

Andreani tracking codes must follow these rules:
- **Exactly 15 digits**
- **Must start with "36000"**
- **Only numeric characters**

Examples of valid codes:
- `360002431028980`
- `360002425903320`

## Usage

### Basic Encode

```python
from andreani_qr.qr import QR

qr = QR("360002431028980")
img = qr.encode()
img.save("360002431028980.png")
```

### Custom Output Path and Filename

```python
from pathlib import Path
from andreani_qr.qr import QR

output_dir = Path("/tmp/qr-codes")
output_dir.mkdir(parents=True, exist_ok=True)

qr = QR("360002431028980")
img = qr.encode()
img.save(output_dir / "my-label.png")
```

### Batch Encode

```python
from pathlib import Path
from andreani_qr.qr import QR, InvalidCodeError

codes = ["360002431028980", "360002425903320"]
output_dir = Path("./output")
output_dir.mkdir(exist_ok=True)

for code in codes:
    try:
        qr = QR(code)
        img = qr.encode()
        img.save(output_dir / f"{code}.png")
    except InvalidCodeError as e:
        print(f"Skipping {code}: {e}")
```

## Error Handling

`QR.__init__` raises `InvalidCodeError` for invalid codes. Always handle it:

```python
from andreani_qr.qr import QR, InvalidCodeError

try:
    qr = QR("bad-code")
except InvalidCodeError as e:
    print(f"Validation failed: {e}")
```

Possible error messages:
- `Code must be 15 characters, got <n>`
- `Code must start with '36000', got '<prefix>'`
- `Code must contain only digits`

## API Reference

### `QR(code: str)`

Creates a QR instance. Validates the code on construction.

- **code** - A 15-digit Andreani tracking number starting with `36000`.
- **Raises** `InvalidCodeError` if the code is invalid.

### `QR.encode() -> Image`

Generates and returns a PIL `Image` of the QR code. The image can be saved with `img.save(path)` to any format PIL supports (PNG, JPEG, etc.).

## When to Use This Skill

Use this skill instead of `cli-encode` when:
- Writing Python scripts or applications that generate QR codes
- Integrating QR generation into a larger Python workflow
- Batch processing tracking codes programmatically
- You need access to the PIL Image object (e.g. for further manipulation)
