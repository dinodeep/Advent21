
def parseinput():

    with open("hardinput.txt", "r") as f:
        line = f.readline()
        nums = list(map(int, line.split(",")))

    return nums


def sum1ToN(n):
    return (n * (n + 1)) // 2


def findAlignment(nums):
    # simulate cost for moving crab to each possible position
    costs = [0] * (max(nums) + 1)
    for num in nums:
        for i in range(len(costs)):
            costs[i] += sum1ToN(abs(num - i))

    minCost = min(costs)
    pos = costs.index(minCost)
    return pos, minCost


def main():
    nums = parseinput()
    pos, cost = findAlignment(nums)
    return cost


result = main()
print(result)
