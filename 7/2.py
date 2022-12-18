from collections import defaultdict
import fileinput

TOTAL_FIELD = "TOTAL"
ROOT = "/"
COMMAND_START = '$ '
ENCODE_SEPERATOR = "/"
CD = "cd"
OUT_ONE = ".."
DIRECTORY = "dir"
TOTAL_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000

def encode(path: list[str]) -> str:
    return ENCODE_SEPERATOR.join(path)

def directories(path: list[str]) -> list[str]:
    return [encode(path[:(-i if i > 0 else len(path))]) for i in range(len(path))]


if __name__ == "__main__":
    currPath = [ROOT]
    sizes = defaultdict(lambda: 0)

    for line in fileinput.input():
        line = line.strip()
        if line.startswith(COMMAND_START):
            command = line.removeprefix(COMMAND_START)
            first, second = (command.split(' ') + [None] * 2)[:2]

            if first == CD:
                if second == ROOT:
                    currPath = [ROOT]
                elif second == OUT_ONE:
                    currPath = currPath[:-1]
                else:
                    currPath.append(second)
        else:
            first, second = line.split(' ')
            if first == DIRECTORY:
                continue
            else:
                size = int(first)
                dirs = directories(currPath)
                for dir in dirs:
                    sizes[dir] += size
    
    toFree = NEEDED_SPACE - (TOTAL_SPACE - sizes[ROOT])
    smallestValid = min(filter(lambda x: x >= toFree, sizes.values()))
    print(smallestValid)



