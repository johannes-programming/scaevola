from typing import *
import operator
import sys
import dataclasses
import enum
import functools
import tomllib
from importlib import resources
import types

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
    overwrites:bool = False
    def __call__(self:Self, cls:type)->type:
        funcs:list = self._getgenerals() + self._getspecials()
        funcs.sort(key=self._sortkey)
        f:types.FunctionType
        for f in funcs:
            if self.overwrites or not hasattr(cls, f.__name__):
                setattr(cls, f.__name__, f)
        return cls
    
    
    @staticmethod
    def _getgeneral(key:str, value:str)->types.FunctionType:
        inner:Callable=getattr(operator, key)
        def outer(self:Self, other:Any)->Any:
            "test"
            return inner(type(self)(other), self)
        outer.__doc__ = Util.util.data["operator"]["doc"] % value
        outer.__name__ = "__r%s__" % key.rstrip("_")
        return outer
    
    @classmethod
    def _getgenerals(cls:type) -> list:
        ans:list=list()
        args:tuple
        for args in Util.util.data["operator"]["symbols"].items():
            ans.append(cls._getgeneral(*args))
        return ans 

    @staticmethod
    def _getspecials() -> list:

        def __ge__(self: Self, other: Any) -> Any:
            "This magic method implements self>=other."
            return type(self)(other) <= self

        def __gt__(self: Self, other: Any) -> Any:
            "This magic method implements self>other."
            return type(self)(other) < self

        def __rdivmod__(self: Self, other: Any) -> Any:
            "This magic method implements divmod(other, self)."
            return divmod(type(self)(other), self)
        
        return [__ge__, __gt__, __rdivmod__]
    
    @staticmethod
    def _sortkey(value:types.FunctionType) -> str:
        return value.__name__

@AutoComplete(overwrites=True)
class Scaevola:
    pass