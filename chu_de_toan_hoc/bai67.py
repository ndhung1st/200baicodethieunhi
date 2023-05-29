n = int(input())
m = 1
while 2**m < n:
    m += 1
m -= 1
print(m, n - 2**m)