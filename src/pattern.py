from dataclasses import dataclass
from line import Line
from point import Point


@dataclass(eq=False)
class Pattern:
    lines: list[Line]
    points: list[Point]
    duration: float
