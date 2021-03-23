import math

from pattern import Pattern
from point import Point
from line import Line

def generate(siteswap, throw_time = 1, dwell_time = 0.2):
    # keep the hands constant
    # keep the props constant
    # have multiple props for each throw
    # integer multiple of siteswap
    max_throw = max(*(throw for item in siteswap for throw in item))
    long_siteswap = siteswap * math.lcm(2, 1 + max_throw//len(siteswap))
    print(long_siteswap)

    beat_time = throw_time + dwell_time

    pattern = Pattern(
        points = [
            Point(
                time = i * beat_time + ct * dwell_time,
                hand = i % 2
            )
            for i in range(len(long_siteswap))
            for ct in range(2)
        ],
        lines = [],
        duration = beat_time * len(long_siteswap)
    )

    for i, item in enumerate(long_siteswap):
        if all(throw == 0 for throw in item):
            continue
        
        pattern.lines.append(Line(
            start = pattern.points[i * 2],
            end = pattern.points[i * 2 + 1],
            color = 0
        ))
        
        for throw in item:
            pattern.lines.append(Line(
                start = pattern.points[i * 2 + 1],
                end = pattern.points[((i + throw) * 2 - 1) % len(pattern.points)],
                color = 1
            ))

    return pattern

if __name__ == '__main__':
    print(generate([[4], [2], [3]], throw_time = 1/30, dwell_time = 4/30))
    # print(generate([[5], [3], [1]]))
