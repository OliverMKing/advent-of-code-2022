from collections import defaultdict

signal = input().strip()
latest = defaultdict(lambda: 0)
lastN = 4
currDuplicates = 0

for i, char in enumerate(signal):
    latest[char] += 1

    if latest[char] == 2:
        currDuplicates += 1
    
    removeI = i - lastN
    if removeI < 0:
        continue

    removeChar = signal[removeI]
    latest[removeChar] -= 1
    if latest[removeChar] == 1:
        currDuplicates -= 1
    
    if currDuplicates == 0:
        print(i + 1)
        break
