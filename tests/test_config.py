"""Tests for config module."""

from types import ModuleType

import pytest
from qrcode.constants import ERROR_CORRECT_L

MAX_QR_VERSION = 40


class TestConfigConstants:
    """Test configuration constants."""

    @pytest.fixture
    def config(self) -> ModuleType:
        """Load the config module."""
        from andreani_qr import config

        return config

    def test_box_size_is_positive_integer(self, config: ModuleType) -> None:
        """BOX_SIZE should be a positive integer."""
        assert isinstance(config.BOX_SIZE, int)
        assert config.BOX_SIZE > 0

    def test_fill_color_is_string(self, config: ModuleType) -> None:
        """FILL_COLOR should be a string."""
        assert isinstance(config.FILL_COLOR, str)

    def test_back_color_is_string(self, config: ModuleType) -> None:
        """BACK_COLOR should be a string."""
        assert isinstance(config.BACK_COLOR, str)

    def test_border_size_is_non_negative_integer(self, config: ModuleType) -> None:
        """BORDER_SIZE should be a non-negative integer."""
        assert isinstance(config.BORDER_SIZE, int)
        assert config.BORDER_SIZE >= 0

    def test_version_is_valid_qr_version(self, config: ModuleType) -> None:
        """VERSION should be between 1 and 40."""
        assert isinstance(config.VERSION, int)
        assert 1 <= config.VERSION <= MAX_QR_VERSION

    def test_error_correction_is_valid_level(self, config: ModuleType) -> None:
        """ERROR_CORRECTION should be a valid QR error correction level."""
        assert config.ERROR_CORRECTION == ERROR_CORRECT_L


class TestConfigLogger:
    """Test logger configuration."""

    @pytest.fixture
    def config(self) -> ModuleType:
        """Load the config module."""
        from andreani_qr import config

        return config

    def test_logger_exists(self, config: ModuleType) -> None:
        """Logger should be configured."""
        assert config.logger is not None

    def test_logger_has_correct_name(self, config: ModuleType) -> None:
        """Logger should have the correct name."""
        assert config.logger.name == "andreani_qr"
