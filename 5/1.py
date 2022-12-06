from collections import deque
import fileinput

stacks = [
    deque(('S', 'T', 'H', 'F', 'W', 'R')),
    deque(('S', 'G', 'D', 'Q', 'W')),
    deque(('B', 'T', 'W')),
    deque(('D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J')),
    deque(('F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z')),
    deque(('L', 'P', 'T', 'C', 'V', 'B', 'S', 'G')),
    deque(('Z', 'B', 'R', 'T', 'W', 'G', 'P')),
    deque(('N', 'G', 'M', 'T', 'C', 'J', 'R')),
    deque(('L', 'G', 'B', 'W'))
]

if __name__ == "__main__":
        for line in fileinput.input():
            _, count, _, fromI, _, toI = line.strip().split(' ')
            count, fromI, toI = map(int, (count, fromI, toI))
            fromI -= 1
            toI -= 1

            for _ in range(count):
                stacks[toI].append(stacks[fromI].pop())

        print(''.join(s[-1] for s in stacks))
