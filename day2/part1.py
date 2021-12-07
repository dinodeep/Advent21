
hPos = 0
depth = 0

with open("input1.txt", "r") as f:
    lines = f.readlines()
    split_lines = [line.split(" ") for line in lines]

for command, val in split_lines:
    if command == "forward":
        hPos += int(val)
    elif command == "down":
        depth += int(val)
    elif command == "up":
        depth = max(0, depth - int(val))

print(hPos * depth)
