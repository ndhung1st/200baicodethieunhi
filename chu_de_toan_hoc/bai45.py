n, m = map(int, input().split())
time = 0
while n > 0:
    time += 1
    n -= 1
    if time % m == 0:
        n += 1
print(time)