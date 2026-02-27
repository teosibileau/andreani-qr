"""Command-line interface to generate Andreani QR codes."""

import click

from andreani_qr.config import logger
from andreani_qr.qr import QR, InvalidCodeError


@click.group
def cli() -> None:
    """Andreani QR cli."""


@cli.command()
@click.argument("code", type=str)
@click.option(
    "--output",
    "-o",
    default=".",
    type=click.Path(),
    help="Output dir for the generated QR code (default: .).",
)
@click.option(
    "--name",
    "-n",
    default="",
    type=str,
    help="Name of the QR code (default: empty).",
)
def encode(code: str, output: str, name: str) -> None:
    """Encode provided TEXT into a QR and save it as an image file."""
    try:
        qr = QR(code)
    except InvalidCodeError as e:
        logger.error(str(e))
        raise SystemExit(1) from None

    img = qr.encode()
    filename = name if name else code
    output_file = f"{output}/{filename}.png"
    img.save(output_file)
    logger.info("QR code generated and saved to %s", output_file)


@cli.command()
@click.argument("qrfile", type=click.Path(exists=True))
def read(qrfile: str) -> None:
    """Read QR code from the provided image file."""
    try:
        qr = QR.from_file(qrfile)
    except InvalidCodeError as e:
        logger.error(str(e))
        raise SystemExit(1) from None

    logger.info("Type: QRCODE, Data: %s", qr.code)


if __name__ == "__main__":
    logger.info("Init")
    cli()
