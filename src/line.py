from point import Point
from dataclasses import dataclass


@dataclass(eq=False)
class Line:
    start: Point
    end: Point
    color: int

    def is_point_inside(self, _time: float):
        if not self.does_line_wrap():
            if self.start.time < _time < self.end.time:
                return True
        else:
            if self.start.time < _time or _time < self.end.time:
                return True
        return False

    def does_line_wrap(self):
        if self.end.time < self.start.time:
            return True
        else:
            return False

    def get_duration(self):
        if self.does_line_wrap():
            return self.end.time + self.start.time - 1
        else:
            return self.start.time - self.end.time
