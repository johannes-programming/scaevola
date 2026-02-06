import builtins
import operator
from typing import *

import setdoc

__all__ = ["Scaevola"]

class Scaevola:

    __slots__ = ()

    @setdoc.basic
    def __ge__(self: Self, other: Any) -> Any:
        return operator.le(type(self)(other), self)

    @setdoc.basic
    def __gt__(self: Self, other: Any) -> Any:
        return operator.lt(type(self)(other), self)

    @setdoc.basic
    def __radd__(self: Self, other: Any) -> Any:
        return operator.add(type(self)(other), self)

    @setdoc.basic
    def __rand__(self: Self, other: Any) -> Any:
        return operator.and_(type(self)(other), self)

    @setdoc.basic
    def __rdivmod__(self: Self, other: Any) -> Any:
        return builtins.divmod(type(self)(other), self)

    @setdoc.basic
    def __rfloordiv__(self: Self, other: Any) -> Any:
        return operator.floordiv(type(self)(other), self)

    @setdoc.basic
    def __rlshift__(self: Self, other: Any) -> Any:
        return operator.lshift(type(self)(other), self)

    @setdoc.basic
    def __rmatmul__(self: Self, other: Any) -> Any:
        return operator.matmul(type(self)(other), self)

    @setdoc.basic
    def __rmod__(self: Self, other: Any) -> Any:
        return operator.mod(type(self)(other), self)

    @setdoc.basic
    def __rmul__(self: Self, other: Any) -> Any:
        return operator.mul(type(self)(other), self)

    @setdoc.basic
    def __ror__(self: Self, other: Any) -> Any:
        return operator.or_(type(self)(other), self)

    @setdoc.basic
    def __rpow__(self: Self, other: Any) -> Any:
        return operator.pow(type(self)(other), self)

    @setdoc.basic
    def __rrshift__(self: Self, other: Any) -> Any:
        return operator.rshift(type(self)(other), self)

    @setdoc.basic
    def __rsub__(self: Self, other: Any) -> Any:
        return operator.sub(type(self)(other), self)

    @setdoc.basic
    def __rtruediv__(self: Self, other: Any) -> Any:
        return operator.truediv(type(self)(other), self)

    @setdoc.basic
    def __rxor__(self: Self, other: Any) -> Any:
        return operator.xor(type(self)(other), self)