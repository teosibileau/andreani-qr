---
name: cli-read
description: "Decode and extract tracking numbers from Andreani QR code images using the andreani-qr CLI. Use when users have QR code images and need to read the embedded tracking codes, debug QR codes, or verify QR content."
---

# Andreani QR Read - Decode QR Code Images

Extract Andreani tracking numbers from QR code images.

## Prerequisites

The andreani-qr package must be installed:

```bash
pipx install git+https://github.com/teosibileau/andreani-qr.git
```

## Supported Image Formats

Any image format supported by PIL (Pillow):
- PNG (`.png`)
- JPEG/JPG (`.jpg`, `.jpeg`)
- BMP (`.bmp`)
- GIF (`.gif`)
- TIFF (`.tiff`)
- And others

## Commands

### Basic Usage

Read a QR code from an image file:

```bash
andreani-qr read ~/Downloads/code.jpeg
```

**Output:**
```
2024-12-08 11:00:50 hostname andreani_qr[6948] INFO Type: QRCODE, Data: 360002425903320
```

### From Current Directory

```bash
andreani-qr read ./360002431028980.png
```

### With Absolute Path

```bash
andreani-qr read /Users/username/Documents/andreani-qr.png
```

## Output Format

The command outputs:
```
Type: QRCODE, Data: <tracking-number>
```

Where:
- **Type:** Always "QRCODE" for valid QR codes
- **Data:** The extracted tracking number (e.g., `360002425903320`)

## Error Handling

### File Not Found

If the image file doesn't exist:
```
Usage: andreani-qr read [OPTIONS] QRFILE
Try 'andreani-qr read --help' for help.

Error: Invalid value for 'QRFILE': Path '<path>' does not exist.
```

### Invalid QR Code

If the image doesn't contain a valid QR code or the QR format is not recognized:
```
ERROR: <error message from pyzbar>
```

### Unreadable Image

If the image is corrupted or in an unsupported format:
```
ERROR: cannot identify image file '<path>'
```

## When to Use This Skill

Use this skill when:
- Debugging QR codes to verify they contain correct tracking numbers
- Processing scanned QR images to extract tracking data
- Verifying QR code generation worked correctly
- Building automation workflows that need to read QR content
- Quality assurance testing of printed QR labels

## Tips

- Ensure the QR code is clearly visible and not blurry in the image
- Good lighting and focus improve detection accuracy
- The tool reads the first QR code found in the image
- Works with both digital images and scanned documents
- Can be used in scripts for batch processing multiple images

## Workflow Example

### Verify Generated QR Code

After generating a QR code, verify it contains the correct tracking number:

```bash
# Generate QR
andreani-qr encode 360002431028980

# Verify content
andreani-qr read ./360002431028980.png
```

Expected output:
```
Type: QRCODE, Data: 360002431028980
```

This confirms the QR code was generated correctly and contains the expected tracking number.
