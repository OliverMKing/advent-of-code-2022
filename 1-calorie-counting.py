import fileinput

maxCalories = 0
currElf = 0

for line in fileinput.input():
    cleanedLine = line.strip()
    if cleanedLine.isdigit():
        currElf += int(cleanedLine)
    else:
        maxCalories = max(maxCalories, currElf)
        currElf = 0
maxCalories = max(maxCalories, currElf)

print(maxCalories)