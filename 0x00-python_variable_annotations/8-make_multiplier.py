#!/usr/bin/env python3
"""A module to retrn a function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function to return a funtion"""
    def fun(n: float) -> float:
        """The returned function"""
        return n * multiplier
    return fun
