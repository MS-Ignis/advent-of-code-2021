count = 0
arr2 = []

with open("input one-one.txt", 'r') as f:
    arr = list(map(int, f.readlines()))
    for i in range(len(arr)):
        try:
            arr2.append(sum(arr[i:i+3]))
        except:
            break

for i in range(1, len(arr2)):
        if arr2[i] > arr2[i-1]:
            count += 1

print(count)