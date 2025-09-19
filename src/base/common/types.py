from typing import Any, Self

import msgspec
from msgspec.structs import fields

from .abc import JsonBytes, JsonString
from .raises import raises


class BaseStruct(msgspec.Struct):
    """Base class for structured data models."""

    @raises(ValueError)
    def to_dict(
        self,
        include: set[str] | None = None,
        exclude: set[str] | None = None,
        exclude_none: bool = False,
    ) -> dict[str, Any]:
        """Convert the struct to a dictionary."""
        attrs = fields(self)

        if include and exclude:
            raise ValueError("Cannot specify both include and exclude")

        attr_names = {attr.name for attr in attrs}

        if include:
            attr_names = include

        if exclude:
            attr_names -= attr_names

        if exclude_none:
            attr_names -= {name for name in attr_names if getattr(self, name, None) is None}

        return {name: getattr(self, name) for name in attr_names}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        """Create an instance of the struct from a dictionary."""
        return msgspec.convert(data, type=cls)

    def to_json(self) -> JsonString:
        """Convert the struct to a JSON string."""
        return msgspec.json.encode(self).decode("utf-8")

    @classmethod
    def from_json(cls, data: JsonString) -> Self:
        """Create an instance of the struct from a JSON string."""
        return msgspec.json.decode(data, type=cls)

    def to_jsonb(self) -> JsonBytes:
        """Convert the struct to a JSONB string."""
        return msgspec.json.encode(self)

    @classmethod
    def from_jsonb(cls, data: JsonBytes) -> Self:
        """Create an instance of the struct from a JSONB string."""
        return msgspec.json.decode(data, type=cls)
