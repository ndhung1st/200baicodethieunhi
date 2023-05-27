def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, int(n ** (1/2)) + 1):
            if n % i == 0:
                return False
        return True
def tinhban(da, bat):
    if snt(da):
        return 0
    if da <= bat:
        return da - 1
    else:
        v = 0
        while bat > 1 and not snt(da):
            if da % bat == 0:
                v += 1
                da -= 1
            else:
                bat -= 1
        return v
arr = []
for i in range(int(input())):
    arr.append(input())
for i in arr:
    t, q, l = map(int, i.split())
    print(tinhban(t,l), tinhban(q,l))