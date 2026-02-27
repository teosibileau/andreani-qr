"""QR code handling for Andreani."""

import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
from qrcode.constants import ERROR_CORRECT_L

from andreani_qr.config import BACK_COLOR, BORDER_SIZE, BOX_SIZE, FILL_COLOR, VERSION


class InvalidCodeError(Exception):
    """Raised when QR code validation fails."""


class QR:
    """QR code handler for Andreani."""

    VALID_PREFIX = "36000"
    CODE_LENGTH = 15

    def __init__(self, code: str) -> None:
        """Initialize QR with a code."""
        self._validate(code)
        self.code = code
        self._image: Image | None = None

    def _validate(self, code: str) -> None:
        if len(code) != self.CODE_LENGTH:
            msg = f"Code must be {self.CODE_LENGTH} characters, got {len(code)}"
            raise InvalidCodeError(msg)
        if not code.startswith(self.VALID_PREFIX):
            msg = f"Code must start with '{self.VALID_PREFIX}', got '{code[:5]}'"
            raise InvalidCodeError(msg)
        if not code.isdigit():
            msg = "Code must contain only digits"
            raise InvalidCodeError(msg)

    def encode(self) -> Image:
        """Generate QR code image."""
        qr = qrcode.QRCode(
            version=VERSION,
            error_correction=ERROR_CORRECT_L,
            box_size=BOX_SIZE,
            border=BORDER_SIZE,
        )
        qr.add_data(self.code)
        qr.make(fit=True)
        self._image = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)
        return self._image

    @classmethod
    def from_file(cls, filepath: str) -> "QR":
        """Create QR instance from an image file."""
        image = Image.open(filepath)
        decoded = decode(image)[0]
        code = decoded.data.decode("utf-8")
        return cls(code)
