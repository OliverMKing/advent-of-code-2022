import fileinput
from typing import NamedTuple
from itertools import chain

Coord = NamedTuple("Coord", [('x', int), ('y', int)])

def visibleOneDirection(line: list[Coord], grid: list[list[chr]]) -> set[chr]:
    v = set()
    prev = -1
    for c in line:
        val = int(grid[c.y][c.x])
        if val <= prev:
            continue
        v.add(c)
        prev = max(prev, val)
    return v


def score(line: list[Coord], grid: list[list[chr]], scores: list[list[int]]):
    for i, coord in enumerate(line):
        val = int(grid[coord.y][coord.x])
        view = len(line) - i - 1
        for j in range(i + 1, len(line)):
            compareCoord = line[j]
            compareVal = int(grid[compareCoord.y][compareCoord.x])
            if val <= compareVal:
                view = j - i
                break

        scores[coord.y][coord.x] *= view if view > 0 else 1




if __name__ == "__main__":
    grid = [list(line.strip()) for line in fileinput.input()]
    height, width = len(grid), len(grid[0])

    scores = [([1] * width) for _ in range(height)]

    for y in range(height):
        line = [Coord(x, y) for x in range(width)]
        score(line, grid, scores)
        score(list(reversed(line)), grid, scores)
    for x in range(width):
        line = [Coord(x, y) for y in range(height)]
        score(line, grid, scores)
        score(list(reversed(line)), grid, scores)


    top = max(chain.from_iterable(scores))
    print(top)

