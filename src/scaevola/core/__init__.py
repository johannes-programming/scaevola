from typing import *
import operator
import sys
import dataclasses
import enum
import functools
import tomllib
from importlib import resources
import types

__all__ = ["Scaevola", "auto", "getfuncnames", "makefunc"]


class Util(enum.Enum):
    util = None

    @functools.cached_property
    def data(self: Self) -> dict:
        "This cached property holds the cfg data."
        text: str = resources.read_text("scaevola.core", "cfg.toml")
        ans: dict = tomllib.loads(text)
        return ans
    
    @functools.cached_property
    def funcdata(self:Self)->dict:
        ans:dict = dict()
        name:str
        doc:str
        inner:Callable
        name="__ge__"
        doc = self.data["docs"]["ge"]
        inner = operator.le
        ans[name] = dict(doc=doc, inner=inner)
        name="__gt__"
        doc = self.data["docs"]["gt"]
        inner = operator.lt
        ans[name] = dict(doc=doc, inner=inner)
        name= "__rdivmod__"
        doc = self.data["docs"]["rdivmod"]
        inner = divmod
        ans[name] = dict(doc=doc, inner=inner)
        x:Any
        y:Any
        for x,y in self.data["operator"].items():
            name = "__r%s__" % x.rstrip("_")
            doc = self.data["docs"]["operator"] % y
            inner = getattr(operator, x)
            ans[name] = dict(doc=doc, inner=inner)
        ans = dict(sorted(ans.items()))
        return ans

     
def auto(cls:type)->type:
    name:str
    for name in getfuncnames():
        if name not in cls.__dict__.keys():
            makefunc(cls, name)
    return cls
   
def getfuncnames() -> list[str]:
    return list(Util.util.funcdata.keys())
    
def makefunc(cls:type, name:str)->types.FunctionType:
    inner:Callable = Util.util.funcdata[name]["inner"]
    def outer(self:Self, other:Any)->Any:
        "This docstring will be overwritten."
        return inner(type(self)(other), self)
    outer.__doc__ = Util.util.funcdata[name]["doc"]
    outer.__module__ = cls.__module__
    outer.__name__ = name
    outer.__qualname__ = cls.__qualname__ + "." + name
    setattr(cls, name, outer)
    return outer

@auto
class Scaevola:
    pass