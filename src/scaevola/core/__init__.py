import builtins
import enum
import functools
import operator
import tomllib
import types
from importlib import resources
from typing import *

import setdoc

__all__ = ["Scaevola", "auto", "getfuncnames", "makefunc"]


class Util(enum.Enum):
    "This enum provides a singleton."

    util = None

    @functools.cached_property
    def data(self: Self) -> dict:
        "This cached property holds the cfg data."
        text: str
        text = resources.read_text("scaevola.core", "cfg.toml")
        return tomllib.loads(text)


def auto(cls: type) -> type:
    "This decorator implements all the righthand functions."
    name: str
    for name in getfuncnames():
        if name not in cls.__dict__.keys():
            makefunc(cls, name)
    return cls


def getfuncnames() -> list[str]:
    "This function returns the names of all righthand functions."
    return list(Util.util.data.keys())


def makefunc(cls: type, name: str) -> types.FunctionType:
    "This function implements a certain righthand function."
    funcname: str
    inner: Callable
    module: Any
    funcname = Util.util.data[name]["func"]
    if Util.util.data[name].get("isbuiltin", False):
        module = builtins
    else:
        module = operator
    inner = getattr(module, funcname)

    def outer(self: Self, other: Any) -> Any:
        "This docstring will be overwritten."
        return inner(type(self)(other), self)

    outer.__module__ = cls.__module__
    outer.__name__ = name
    outer.__qualname__ = cls.__qualname__ + "." + name
    setdoc.basic(outer)
    setattr(cls, name, outer)
    return outer


@auto
class Scaevola:
    __slots__ = ()
