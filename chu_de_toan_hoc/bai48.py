n = int(input())
np = int(n ** (1/2))
arr = [1] * (n + 1)
arr[0] = arr[1] = 0
def sntt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True
for i in range(2, int(np ** (1/2)) + 1):
    for j in range(i ** 2, np + 1, i):
        arr[j] = 0
snt = []
for i in range(np + 1):
    if arr[i] == 1:
        snt.append(i)
kt = True
for i in snt:
    if sntt(4 + i**2) and 4 + i**2 <= n:
        print(2, i, 4 + i**2)
        kt = False
if kt:
    print(-1)