import unittest
from typing import *

from scaevola.core import Scaevola

__all__=["TestSlots"]

class Foo(Scaevola):
    __slots__ = ("x", "y")


class Bar(Scaevola):
    pass


class TestSlots(unittest.TestCase):
    def test_foo(self: Self) -> None:
        foo: Foo
        foo = Foo()
        foo.x = 4
        foo.y = 2
        self.assertEqual(foo.x, 4)
        self.assertEqual(foo.y, 2)

    def test_bar(self: Self) -> None:
        bar: Bar
        bar = Bar()
        bar.x = 4
        bar.y = 2
        self.assertEqual(bar.x, 4)
        self.assertEqual(bar.y, 2)


if __name__ == "__main__":
    unittest.main()
