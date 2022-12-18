import fileinput
from typing import NamedTuple

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


def visible(line: list[Coord], grid: list[list[chr]]) -> set[chr]:
    return visibleOneDirection(line, grid) | visibleOneDirection(reversed(line), grid)


if __name__ == "__main__":
    grid = [list(line.strip()) for line in fileinput.input()]
    height, width = len(grid), len(grid[0])

    v = set()
    for y in range(height):
        line = [Coord(x, y) for x in range(width)]
        v |= visible(line, grid)
    for x in range(width):
        line = [Coord(x, y) for y in range(height)]
        v |= visible(line, grid)
    
    print(len(v))

