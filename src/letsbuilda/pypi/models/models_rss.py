"""Models for RSS responses"""

from dataclasses import dataclass
from datetime import datetime


def _parse_publication_date(publication_date: str) -> datetime:
    return datetime.strptime(publication_date, "%a, %d %b %Y %H:%M:%S %Z")


@dataclass(frozen=True, slots=True)
class RSSPackageMetadata:
    """RSS Package metadata"""

    title: str
    version: str | None
    package_link: str
    guid: str
    description: str | None
    author: str | None
    publication_date: datetime | None

    @classmethod
    def build_from(cls, data: dict[str, str]) -> "RSSPackageMetadata":
        """Build an instance from raw data"""
        split_title = data.get("title").removesuffix(" added to PyPI").split()
        title = split_title[0]
        if len(split_title) == 2:
            version = split_title[1]
        else:
            version = None

        publication_date: str | None = data.get("pubDate")
        if publication_date is not None:
            publication_date: datetime = _parse_publication_date(publication_date)

        return cls(
            title=title,
            version=version,
            package_link=data.get("link"),
            guid=data.get("guid"),
            description=data.get("description"),
            author=data.get("author"),
            publication_date=publication_date,
        )
