n = int(input())
tong = 1
for i in range(2, int(n ** (1/2)) + 1):
    if n % i == 0:
        tong += i + n // i
if tong > n:
    print(1)
else:
    print(0)