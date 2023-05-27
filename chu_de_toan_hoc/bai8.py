arr = []
for i in range(int(input())):
    arr.append(int(input()))
for i in arr:
    print((i - 1) % 2)