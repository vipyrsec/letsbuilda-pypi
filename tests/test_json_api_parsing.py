"""Test parsing metadata from the JSON API."""

from __future__ import annotations

import json
from pathlib import Path

from letsbuilda.pypi import JSONPackageMetadata


def test_json_api_data_parsing() -> None:
    """Confirm sample JSON API data gets parsed correctly."""
    text = (Path(__file__).parent / "json_api_response.json").read_text(encoding="UTF=8")
    model = JSONPackageMetadata.from_dict(json.loads(text))

    assert model.info.name == "letsbuilda-pypi"
    assert model.info.version == "4.0.0"
