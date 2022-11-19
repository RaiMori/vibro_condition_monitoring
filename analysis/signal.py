import numpy
from typing import NamedTuple

class Signal(NamedTuple):
    raw: numpy.array
    fs: float