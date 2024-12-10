"""Command-line interface to generate Andreani QR codes."""

import click
import qrcode
from config import BACK_COLOR, BORDER_SIZE, BOX_SIZE, ERROR_CORRECTION, FILL_COLOR, VERSION, logger
from PIL import Image
from pyzbar.pyzbar import decode


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
def encode(code: str, output: str) -> None:
    """Encode provided TEXT into a QR and save it as an image file."""
    logger.info("Processing %s", code)
    logger.info(
        "Instantiating QR code with version:%s error_correction:%s box_size:%s border:%s",
        VERSION,
        ERROR_CORRECTION,
        BOX_SIZE,
        BORDER_SIZE,
    )
    qr = qrcode.QRCode(
        version=VERSION,
        error_correction=ERROR_CORRECTION,
        box_size=BOX_SIZE,
        border=BORDER_SIZE,
    )

    logger.info("Adding data to QR")
    qr.add_data(code)
    qr.make(fit=True)

    logger.info("Generating QR code with fill: %s and back:%s", FILL_COLOR, BACK_COLOR)
    img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)

    output_file = f"{output}/{code}.png"
    logger.info("Saving QR code to %s", output_file)
    img.save(output_file)
    logger.info("QR code generated and saved to %s", output_file)


@cli.command()
@click.argument("qrfile", type=click.Path(exists=True))
def read(qrfile: str) -> None:
    """Read QR code from the provided image file."""
    # Load the QR code image
    qr_image = Image.open(qrfile)
    decoded_objects = decode(qr_image)

    for obj in decoded_objects:
        logger.info("Type: %s, Data: %s", obj.type, obj.data.decode("utf-8"))


if __name__ == "__main__":
    logger.info("Init")
    cli()
