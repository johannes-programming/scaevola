import unittest
from typing import *

from scaevola.core import Scaevola

__all__ = ["TestScaevola"]


# Subclass of Scaevola to implement basic arithmetic and comparison operations
class ScaevolaSubclass(Scaevola):
    def __init__(self: Self, value: Any) -> Any:
        self.value = value

    def __eq__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return self.value == other.value
        raise NotImplementedError

    def __lt__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return self.value < other.value
        raise NotImplementedError

    def __le__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return self.value <= other.value
        raise NotImplementedError

    def __add__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value + other.value)
        raise NotImplementedError

    def __and__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value & other.value)
        raise NotImplementedError

    def __divmod__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return divmod(self.value, other.value)
        raise NotImplementedError

    def __floordiv__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value // other.value)
        raise NotImplementedError

    def __lshift__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value << other.value)
        raise NotImplementedError

    def __matmul__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(
                self.value * other.value
            )  # Simulating matrix multiplication
        raise NotImplementedError

    def __mod__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value % other.value)
        raise NotImplementedError

    def __mul__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value * other.value)
        raise NotImplementedError

    def __or__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value | other.value)
        raise NotImplementedError

    def __pow__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value**other.value)
        raise NotImplementedError

    def __rshift__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value >> other.value)
        raise NotImplementedError

    def __sub__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value - other.value)
        raise NotImplementedError

    def __truediv__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value / other.value)
        raise NotImplementedError

    def __xor__(self: Self, other: Any) -> Any:
        if isinstance(other, ScaevolaSubclass):
            return ScaevolaSubclass(self.value ^ other.value)
        raise NotImplementedError


class TestScaevola(unittest.TestCase):
    def setUp(self: Self) -> None:
        self.obj1 = ScaevolaSubclass(10)
        self.obj2 = ScaevolaSubclass(20)

    def test_ge(self: Self) -> None:
        self.assertTrue(self.obj2 >= 10)
        self.assertFalse(self.obj1 >= 20)

    def test_gt(self: Self) -> None:
        self.assertTrue(self.obj2 > 10)
        self.assertFalse(self.obj1 > 20)

    def test_radd(self: Self) -> None:
        result = 15 + self.obj1
        self.assertEqual(result.value, 25)

    def test_rand(self: Self) -> None:
        result = 15 & self.obj1
        self.assertEqual(result.value, 10 & 15)

    def test_rdivmod(self: Self) -> None:
        result = divmod(25, self.obj1)
        self.assertEqual(result, (2, 5))

    def test_rfloordiv(self: Self) -> None:
        result = 25 // self.obj1
        self.assertEqual(result.value, 2)

    def test_rlshift(self: Self) -> None:
        result = 2 << self.obj1
        self.assertEqual(result.value, 2 << 10)

    def test_rmatmul(self: Self) -> None:
        result = 2 @ self.obj1
        self.assertEqual(result.value, 2 * 10)

    def test_rmod(self: Self) -> None:
        result = 23 % self.obj1
        self.assertEqual(result.value, 23 % 10)

    def test_rmul(self: Self) -> None:
        result = 2 * self.obj1
        self.assertEqual(result.value, 20)

    def test_ror(self: Self) -> None:
        result = 2 | self.obj1
        self.assertEqual(result.value, 2 | 10)

    def test_rpow(self: Self) -> None:
        result = 2**self.obj1
        self.assertEqual(result.value, 2**10)

    def test_rrshift(self: Self) -> None:
        result = 1024 >> self.obj1
        self.assertEqual(result.value, 1024 >> 10)

    def test_rsub(self: Self) -> None:
        result = 25 - self.obj1
        self.assertEqual(result.value, 25 - 10)

    def test_rtruediv(self: Self) -> None:
        result = 100 / self.obj1
        self.assertEqual(result.value, 100 / 10)

    def test_rxor(self: Self) -> None:
        result = 15 ^ self.obj1
        self.assertEqual(result.value, 15 ^ 10)


if __name__ == "__main__":
    unittest.main()
