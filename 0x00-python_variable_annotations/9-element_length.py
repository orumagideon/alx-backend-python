#!/usr/bin/env python3
"""Function with annotated parameters and
return values with appropriate types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """ List of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]
