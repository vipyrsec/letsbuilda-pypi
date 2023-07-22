"""Custom exceptions."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Self


class PackageNotFoundError(Exception):
    """Raised when a package is not found."""

    def __init__(self: Self, package_title: str, package_version: str | None) -> None:
        """Initialize the superclass with the appropriate information."""
        self.package_title = package_title
        self.package_version = package_version
        super().__init__(
            f"'{self.package_title}' @ '{self.package_version}' not found on PyPI!",
        )
