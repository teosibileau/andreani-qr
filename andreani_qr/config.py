"""Config module for the project."""

import logging

import coloredlogs
from qrcode.constants import ERROR_CORRECT_L

logger = logging.getLogger("andreani_qr")
coloredlogs.install(level="INFO", logger=logger)

BOX_SIZE = 21
FILL_COLOR = "black"
BACK_COLOR = "white"
BORDER_SIZE = 4
VERSION = 1  # Controls the size of the QR Code
ERROR_CORRECTION = ERROR_CORRECT_L  # Error correction level
