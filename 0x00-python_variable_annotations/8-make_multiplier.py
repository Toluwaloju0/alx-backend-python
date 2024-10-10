#!/usr/bin/python3
"""A module to retrn a function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def fun(n: float) -> float:
        return n * multiplier