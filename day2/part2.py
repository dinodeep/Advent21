
hPos = 0
depth = 0
aim = 0

with open("input2.txt", "r") as f:
    lines = f.readlines()
    split_lines = [line.split(" ") for line in lines]

for command, val in split_lines:
    if command == "forward":
        hPos += int(val)
        depth += aim * int(val)
    elif command == "down":
        aim += int(val)
    elif command == "up":
        aim -= int(val)

print(hPos * depth)
