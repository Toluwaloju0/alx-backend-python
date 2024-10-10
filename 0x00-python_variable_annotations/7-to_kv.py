#!/usr/bin/env python3
"""A module to create a tuple"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """A function to create a tuple
    Args:
        k(str): A string in the tuple
        v(int, float): a number in the tuple
    Return: A tuple containing k and v
    """

    return (k, v ** 2)
