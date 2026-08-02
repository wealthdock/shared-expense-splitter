"""Smoke tests for the package."""

import shared_expense_splitter as pkg


def test_package_importable() -> None:
    assert pkg is not None


def test_version_exposed() -> None:
    assert pkg.__version__ == "0.1.0"
