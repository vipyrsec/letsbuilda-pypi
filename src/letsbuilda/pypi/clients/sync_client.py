"""The sync client."""

from io import BytesIO
from typing import Final, Self

import xmltodict
from requests import Session

from letsbuilda.pypi.models import JSONPackageMetadata, RSSPackageMetadata


class PyPIServices:
    """A class for interacting with PyPI."""

    NEWEST_PACKAGES_FEED_URL: Final[str] = "https://pypi.org/rss/packages.xml"
    PACKAGE_UPDATES_FEED_URL: Final[str] = "https://pypi.org/rss/updates.xml"

    def __init__(self: Self, http_session: Session) -> None:
        self.http_session = http_session

    def get_rss_feed(self: Self, feed_url: str) -> list[RSSPackageMetadata]:
        """Get the new packages RSS feed."""
        response_text = self.http_session.get(feed_url).text
        rss_data = xmltodict.parse(response_text)["rss"]["channel"]["item"]
        return [RSSPackageMetadata.build_from(package_data) for package_data in rss_data]

    def get_package_metadata(
        self: Self,
        package_name: str,
        package_version: str | None = None,
    ) -> JSONPackageMetadata:
        """Get metadata for a package."""
        if package_version is not None:
            url = f"https://pypi.org/pypi/{package_name}/{package_version}/json"
        else:
            url = f"https://pypi.org/pypi/{package_name}/json"
        response_dict = self.http_session.get(url).json()
        return JSONPackageMetadata.from_dict(response_dict)

    def fetch_bytes(
        self: Self,
        url: str,
    ) -> BytesIO:
        """Fetch bytes from a URL."""
        response = self.http_session.get(url)
        buffer = BytesIO(response.content)
        buffer.seek(0)
        return buffer
