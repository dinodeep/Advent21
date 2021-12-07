
with open("input1.txt", "r") as f:
    lines = f.readlines()
    nums = [int(line) for line in lines]

increaseCount = 0
for i in range(1, len(nums)):
    if nums[i - 1] < nums[i]:
        increaseCount += 1
print(increaseCount)
