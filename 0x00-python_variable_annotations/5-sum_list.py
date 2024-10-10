#!/usr/bin/env python3
"""A module to add a list of floats"""


def sum_list(input_list: list[float]) -> float:
    """A function to add floats toghther
    Args:
        input_list(list of floats): Th elist containg the floats
    Return: Addition of all float numbers
    """

    a: float = 0

    for num in input_list:
        a += num

    return a
