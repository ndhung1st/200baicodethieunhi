n, a = map(int, input().split())
if a % 2 == 0:
    a = n - a + 1
print((a - 1)//2 + 1)