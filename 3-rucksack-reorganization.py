import fileinput

def duplicate(str1: str, str2: str) -> chr:
    seen = set(c for c in str1)
    for c in str2:
        if c in seen:
            return c
    
    raise Exception("No duplicate found")

def point(c: chr) -> int:
    if (c.isupper()):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


if __name__ == '__main__':
    total = 0

    for line in fileinput.input():
        cleanedLine = line.strip()
        half = len(cleanedLine) // 2
        first, second = cleanedLine[:half], cleanedLine[half:]
        dup = duplicate(first, second)

        total += point(dup)

    print(total)