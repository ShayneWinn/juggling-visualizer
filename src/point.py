from dataclasses import dataclass


@dataclass(eq=False)
class Point:
    time: float
    hand: int
