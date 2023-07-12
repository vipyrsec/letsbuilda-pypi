"""Models for RSS responses."""

from dataclasses import dataclass
from datetime import datetime
from typing import Self


def _parse_publication_date(publication_date: str) -> datetime:
    return datetime.strptime(publication_date, "%a, %d %b %Y %H:%M:%S %Z")  # noqa: DTZ007 - uses `Z` instead of `z`


@dataclass(frozen=True, slots=True)
class RSSPackageMetadata:
    """RSS Package metadata."""

    title: str
    version: str | None
    package_link: str
    guid: str | None
    description: str | None
    author: str | None
    publication_date: datetime

    @classmethod
    def build_from(cls: type[Self], data: dict[str, str]) -> "RSSPackageMetadata":
        """Build an instance from raw data."""
        split_title = data.get("title").removesuffix(" added to PyPI").split()
        title = split_title[0]
        version = split_title[1] if len(split_title) == 2 else None  # noqa: PLR2004 - is not magic

        return cls(
            title=title,
            version=version,
            package_link=data.get("link"),
            guid=data.get("guid"),
            description=data.get("description"),
            author=data.get("author"),
            publication_date=_parse_publication_date(data.get("pubDate")),
        )
