#!/usr/bin/env python3
"""A module to annotate afunction"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """The function to annotate"""
    return [(i, len(i)) for i in lst]
