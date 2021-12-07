from collections import Counter


def parseinput():
    with open("hardtest.txt", "r") as f:
        line = f.readline()

    nums = list(map(int, line.split(",")))
    counts = Counter(nums)
    dayMap = [0] * 9
    for day, count in counts.items():
        dayMap[day] = count

    return dayMap


def nextDay(dayMap):
    # decrease all counters for smaller fish
    endFish = dayMap[0]
    newDayMap = dayMap[1:] + [0]
    newDayMap[6] += endFish
    newDayMap[8] += endFish
    return newDayMap


def main():
    dayMap = parseinput()

    for i in range(80):
        dayMap = nextDay(dayMap)

    return sum(dayMap)


result = main()
print(result)
