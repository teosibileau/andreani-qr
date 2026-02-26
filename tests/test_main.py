"""Tests for main module."""

from pathlib import Path
from types import ModuleType
from unittest.mock import MagicMock, patch

import pytest
from click.testing import CliRunner


class TestCli:
    """Test the CLI group."""

    @pytest.fixture
    def cli(self) -> ModuleType:
        """Load the main module."""
        from andreani_qr import main

        return main

    def test_cli_is_click_group(self, cli: ModuleType) -> None:
        """Verify cli is a Click group."""
        assert cli.cli is not None

    def test_encode_command_exists(self, cli: ModuleType) -> None:
        """Verify the encode command exists."""
        assert hasattr(cli, "encode")
        assert callable(cli.encode)

    def test_read_command_exists(self, cli: ModuleType) -> None:
        """Verify the read command exists."""
        assert hasattr(cli, "read")
        assert callable(cli.read)


class TestEncode:
    """Test the encode command."""

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a Click test runner."""
        return CliRunner()

    @pytest.fixture
    def cli_module(self) -> ModuleType:
        """Load the main module."""
        from andreani_qr import main

        return main

    def test_encode_command_creates_qr(
        self,
        runner: CliRunner,
        cli_module: ModuleType,
        tmp_path: Path,
    ) -> None:
        """Verify QR code is created."""
        with (
            patch("andreani_qr.main.qrcode") as mock_qrcode,
            patch.object(mock_qrcode.QRCode.return_value, "make_image") as mock_make_image,
            patch("andreani_qr.main.logger", MagicMock()),
        ):
            mock_img = MagicMock()
            mock_make_image.return_value = mock_img
            with patch.object(mock_img, "save"):
                result = runner.invoke(cli_module.cli, ["encode", "test_code", "-o", str(tmp_path)])

            assert result.exit_code == 0
            mock_qrcode.QRCode.assert_called_once()

    def test_encode_command_adds_data(
        self,
        runner: CliRunner,
        cli_module: ModuleType,
        tmp_path: Path,
    ) -> None:
        """Verify data is added to QR code."""
        with (
            patch("andreani_qr.main.qrcode") as mock_qrcode,
            patch.object(mock_qrcode.QRCode.return_value, "make_image") as mock_make_image,
            patch("andreani_qr.main.logger", MagicMock()),
        ):
            mock_img = MagicMock()
            mock_make_image.return_value = mock_img
            with patch.object(mock_img, "save"):
                result = runner.invoke(cli_module.cli, ["encode", "test_code", "-o", str(tmp_path)])

            assert result.exit_code == 0
            mock_qrcode.QRCode.return_value.add_data.assert_called_once_with("test_code")

    def test_encode_command_saves_image(
        self,
        runner: CliRunner,
        cli_module: ModuleType,
        tmp_path: Path,
    ) -> None:
        """Verify image is saved."""
        with (
            patch("andreani_qr.main.qrcode") as mock_qrcode,
            patch.object(mock_qrcode.QRCode.return_value, "make_image") as mock_make_image,
            patch("andreani_qr.main.logger", MagicMock()),
        ):
            mock_img = MagicMock()
            mock_make_image.return_value = mock_img
            with patch.object(mock_img, "save") as mock_save:
                result = runner.invoke(cli_module.cli, ["encode", "test_code", "-o", str(tmp_path)])

                assert result.exit_code == 0
                mock_save.assert_called_once()


class TestRead:
    """Test the read command."""

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a Click test runner."""
        return CliRunner()

    @pytest.fixture
    def cli_module(self) -> ModuleType:
        """Load the main module."""
        from andreani_qr import main

        return main

    def test_read_command_decodes_qr(
        self,
        runner: CliRunner,
        cli_module: ModuleType,
        tmp_path: Path,
    ) -> None:
        """Verify QR is decoded."""
        test_file = tmp_path / "test.png"
        test_file.write_text("fake image")

        with (
            patch("andreani_qr.main.Image") as mock_image_class,
            patch("andreani_qr.main.decode") as mock_decode,
            patch("andreani_qr.main.logger", MagicMock()),
        ):
            mock_image = MagicMock()
            mock_image_class.open.return_value = mock_image
            mock_decoded = [MagicMock(data=b"test_data", type="QR")]
            mock_decode.return_value = mock_decoded

            result = runner.invoke(cli_module.cli, ["read", str(test_file)])

            assert result.exit_code == 0
            mock_decode.assert_called_once()
