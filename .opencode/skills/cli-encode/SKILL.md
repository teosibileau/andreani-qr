---
name: cli-encode
description: "Generate QR code images from Andreani tracking numbers using the andreani-qr CLI. Use when users want to create QR codes for Andreani packages, need to encode tracking codes into QR images, or want to customize output filenames and locations."
---

# Andreani QR Encode - Generate QR Codes from Tracking Numbers

Generate QR code images from valid Andreani tracking numbers.

## Prerequisites

The andreani-qr package must be installed:

```bash
pipx install git+https://github.com/teosibileau/andreani-qr.git
```

## Valid Code Format

Andreani tracking codes must follow these rules:
- **Exactly 15 digits**
- **Must start with "36000"**
- **Only numeric characters**

Examples of valid codes:
- `360002431028980`
- `360002425903320`

## Commands

### Basic Usage

Generate a QR code with the tracking number as the filename:

```bash
andreani-qr encode 360002431028980
```

**Output:**
```
2024-12-10 19:02:14 hostname andreani_qr[67683] INFO QR code generated and saved to ./360002431028980.png
```

### Custom Output Directory

Save the QR code to a specific directory:

```bash
andreani-qr encode 360002431028980 -o /path/to/output
```

or using the long option:

```bash
andreani-qr encode 360002431028980 --output /path/to/output
```

### Custom Filename

Specify a custom filename (without extension):

```bash
andreani-qr encode 360002431028980 -n my-custom-name
```

or using the long option:

```bash
andreani-qr encode 360002431028980 --name my-custom-name
```

**Output:**
```
QR code generated and saved to ./my-custom-name.png
```

### Combined Options

Use both custom output directory and filename:

```bash
andreani-qr encode 360002431028980 -o ~/Downloads -n package-qr
```

This creates: `~/Downloads/package-qr.png`

## Error Handling

### Invalid Code Length

If the code doesn't have exactly 15 characters:
```
ERROR: Code must be 15 characters, got 14
```

### Invalid Prefix

If the code doesn't start with "36000":
```
ERROR: Code must start with '36000', got '12345'
```

### Non-numeric Characters

If the code contains letters or special characters:
```
ERROR: Code must contain only digits
```

## Output

- **Format:** PNG image file
- **Default location:** Current working directory
- **Default filename:** The tracking code itself (e.g., `360002431028980.png`)
- **QR Content:** The tracking number as plain text

## When to Use This Skill

Use this skill when:
- Generating QR codes for Andreani package tracking
- Creating printable QR labels for shipments
- Automating QR generation in scripts or workflows
- Batch processing multiple tracking codes

## Tips

- Always validate tracking codes before encoding
- Use custom names when generating multiple QRs to avoid filename conflicts
- The generated PNG files are ready for printing or digital use
