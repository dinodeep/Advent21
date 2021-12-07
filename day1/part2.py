with open("input2.txt", "r") as f:
    lines = f.readlines()
    nums = [int(line) for line in lines]

counts = 0
for i in range(len(nums) - 3):
    if nums[i] < nums[i + 3]:
        counts += 1
print(counts)
