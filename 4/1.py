import fileinput

def parsedLine(line: str):
    cleaned = line.strip()
    elves = cleaned.split(',')
    return [map(int, elf.split('-')) for elf in elves]

if __name__ == '__main__':
    total = 0

    splitInput = [parsedLine(line) for line in fileinput.input()]
    for elf1, elf2 in splitInput:
        elf1Min, elf1Max = elf1
        elf2Min, elf2Max = elf2

        if elf1Max >= elf2Max and elf1Min <= elf2Min:
            total += 1
        elif elf2Max >= elf1Max and elf2Min <= elf1Min:
            total += 1

    print(total)
