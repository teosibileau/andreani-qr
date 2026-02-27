"""Tests for qr module."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from andreani_qr.qr import QR, InvalidCodeError


class TestQRValidation:
    """Test QR code validation."""

    VALID_CODE = "360002827140850"

    def test_valid_code_passes(self) -> None:
        """Verify valid code passes validation."""
        qr = QR(self.VALID_CODE)
        assert qr.code == self.VALID_CODE

    def test_invalid_length_raises(self) -> None:
        """Verify invalid length raises InvalidCodeError."""
        with pytest.raises(InvalidCodeError) as exc_info:
            QR("36000")
        assert "Code must be 15 characters" in str(exc_info.value)

    def test_invalid_prefix_raises(self) -> None:
        """Verify invalid prefix raises InvalidCodeError."""
        with pytest.raises(InvalidCodeError) as exc_info:
            QR("123456789012345")
        assert "Code must start with '36000'" in str(exc_info.value)

    def test_non_digit_raises(self) -> None:
        """Verify non-digit characters raise InvalidCodeError."""
        with pytest.raises(InvalidCodeError) as exc_info:
            QR("36000282714085a")
        assert "Code must contain only digits" in str(exc_info.value)


class TestQRencode:
    """Test QR encode method."""

    def test_encode_returns_image(self) -> None:
        """Verify encode returns an image."""
        qr = QR("360002827140850")
        with patch("andreani_qr.qr.qrcode") as mock_qrcode:
            mock_img = MagicMock()
            mock_qrcode.QRCode.return_value.make.return_value = None
            mock_qrcode.QRCode.return_value.make_image.return_value = mock_img
            result = qr.encode()
            assert result == mock_img


class TestQRFromFile:
    """Test QR from_file class method."""

    def test_from_file_decodes_qr(self) -> None:
        """Verify from_file decodes QR code from file."""
        with (
            patch("andreani_qr.qr.Image") as mock_image,
            patch("andreani_qr.qr.decode") as mock_decode,
        ):
            mock_decoded = MagicMock()
            mock_decoded.data = b"360002827140850"
            mock_decode.return_value = [mock_decoded]

            qr = QR.from_file("test.png")

            assert qr.code == "360002827140850"
            mock_image.open.assert_called_once_with("test.png")
            mock_decode.assert_called_once()
