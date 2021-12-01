count = 0

with open("input one-one.txt", 'r') as f:
    arr = list(map(int, f.readlines()))
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            count += 1

print(count)