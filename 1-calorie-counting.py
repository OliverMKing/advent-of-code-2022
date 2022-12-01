import fileinput

maxCalories = 0
currElf = 0

for line in fileinput.input():
    cleanedLine = line.strip()
    if cleanedLine.isdigit():
        currElf += int(cleanedLine)
        maxCalories = max(maxCalories, currElf)
    else:
        currElf = 0

print(maxCalories)