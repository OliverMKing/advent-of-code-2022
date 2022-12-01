import fileinput
import heapq

best = []
top = 3
currElf = 0

def addToBest(count):
    heapq.heappush(best, count)
    while len(best) > top:
        heapq.heappop(best)

for line in fileinput.input():
    cleanedLine = line.strip()
    if cleanedLine.isdigit():
        currElf += int(cleanedLine)
    else:
        addToBest(currElf)
        currElf = 0
addToBest(currElf)

topSum = sum(best)
print(topSum)
