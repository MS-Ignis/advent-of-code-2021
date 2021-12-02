arr = []
forward = 0
depth = 0
aim = 0

with open("input two-one.txt", 'r') as f:
    data = f.readlines()

    for i in data:
        arr.append(i.split())

for i in arr:
    if i[0] == 'forward':
        forward += int(i[1])
        depth += int(i[1]) * aim
    if i[0] == 'down':
        aim += int(i[1])
    if i[0] == 'up':
        aim -= int(i[1])

print(forward)
print(depth)

print(forward * depth)