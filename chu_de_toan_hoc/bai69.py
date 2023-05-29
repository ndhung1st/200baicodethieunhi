t = int(input())
kk = []
for i in range(t):
    kk.append(input())
for i in range(t):
    n, a, b = map(int, kk[i].split())
    if 1/a > 2/b:
        print(a * n)
    else:
        tien = (n//2)*b + (n%2)*a
        print(tien)