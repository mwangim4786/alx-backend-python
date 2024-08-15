#!/usr/bin/env python3
'''  takes a string k and an int OR float v as arguments and returns a tuple (str, float).
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Outputs tuple consisting of k and the square of v. '''
    return (k, v * v)
