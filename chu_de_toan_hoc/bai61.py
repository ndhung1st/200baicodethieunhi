def tong(x):
    t = 0
    for i in x:
        t += int(i)
    return t
def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True
a = int(input())
if int(a ** (1/2)) ** 2 == a:
    print(int(a ** (1/2)))
elif snt(a):
    print(-1)
else:
    kt = True
    for i in range(1, int(a ** (1/2)) + 1):
        if a % i == 0 and a % tong(str(i)) == 0 and i * tong(str(i)) == a:
            print(i)
            kt = False
            break
    for i in range(int(a ** (1/2)), 0, -17):
        if a % i == 0 and a % tong(str(a//i)) == 0 and a//i * tong(str(a//i)) == a:
            print(a//i)
            kt = False
    if kt:
        print(-1)