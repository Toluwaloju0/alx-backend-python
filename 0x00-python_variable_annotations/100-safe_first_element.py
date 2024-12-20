#!/usr/bin/env python3
"""A module to annotate a any class"""

from typing import Any, Sequence, Tuple, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The function to annotate"""
    if lst:
        return lst[0]
    else:
        return None
