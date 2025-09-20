import builtins
import dataclasses
import enum
import functools
import operator
import tomllib
import types
from importlib import resources
from typing import *

__all__ = ["AutoComplete", "Scaevola"]


class Util(enum.Enum):
    util = None

    @functools.cached_property
    def data(self: Self) -> dict:
        "This cached property holds the cfg data."
        text: str = resources.read_text("scaevola.core", "cfg.toml")
        ans: dict = tomllib.loads(text)
        return ans


@dataclasses.dataclass
class AutoComplete:
    overwrites: bool = False

    def __call__(self: Self, cls: type) -> type:
        funcs: list = self._getfunctions()
        funcs.sort(key=self._sortkey)
        f: types.FunctionType
        for f in funcs:
            if self.overwrites or not hasattr(cls, f.__name__):
                setattr(cls, f.__name__, f)
        return cls

    @staticmethod
    def _getbuiltins(name: str) -> types.FunctionType:
        inner: Any = getattr(builtins, name)

        def outer(self: Self, other: Any) -> Any:
            "This docstring will be overwritten."
            return inner(type(self)(other), self)

        outer.__doc__ = Util.util.data["builtins"]["doc"] % name
        outer.__name__ = "__r%s__" % name
        return outer

    @staticmethod
    def _getoperator(key: str, value: str) -> types.FunctionType:
        inner: Any = getattr(operator, key)

        def outer(self: Self, other: Any) -> Any:
            "This docstring will be overwritten."
            return inner(type(self)(other), self)

        outer.__doc__ = Util.util.data["operator"]["doc"] % value
        outer.__name__ = "__r%s__" % key.rstrip("_")
        return outer

    @staticmethod
    def _getrel(key: str, value: str) -> types.FunctionType:
        inner: Any = getattr(operator, "l" + key)

        def outer(self: Self, other: Any) -> Any:
            "This docstring will be overwritten."
            return inner(type(self)(other), self)

        outer.__doc__ = Util.util.data["operator"]["doc"] % (">" + value)
        outer.__name__ = "__g%s__" % key
        return outer

    @classmethod
    def _getfunctions(cls: type) -> list[types.FunctionType]:
        ans: list = list()
        x: Any
        y: Any
        for x in Util.util.data["builtins"]["names"]:
            ans.append(cls._getbuiltins(x))
        for x, y in Util.util.data["operator"]["symbols"].items():
            ans.append(cls._getoperator(x, y))
        for x, y in Util.util.data["operator"]["rel"].items():
            ans.append(cls._getrel(x, y))
        return ans

    @staticmethod
    def _sortkey(value: Any) -> str:
        return value.__name__


@AutoComplete()
class Scaevola:
    pass
