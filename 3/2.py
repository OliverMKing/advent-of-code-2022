import fileinput

def duplicate(*strs: str) -> chr:
    sets = map(lambda s: set(c for c in s), strs)
    return set(c for c in strs[0]).intersection(*sets).pop()

def point(c: chr) -> int:
    if (c.isupper()):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


if __name__ == '__main__':
    total = 0

    arrInput = [line.strip() for line in fileinput.input()]
    threes = [arrInput[i:i+3] for i in range(0, len(arrInput), 3)]
    for group in threes:
        dup = duplicate(*group)
        total += point(dup)

    print(total)
