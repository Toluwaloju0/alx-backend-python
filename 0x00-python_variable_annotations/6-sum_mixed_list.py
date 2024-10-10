#!/usr/bin/env python3
"""A modulr to add a mixed list of intgers and floats"""

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """A function to add a list of integers and floats
    Args:
        mxd_lst(list): A list of integers and floats
    Return: A float of the answer
    """

    sum: float = 0
    for a in mxd_lst:
        sum += a

    return sum
