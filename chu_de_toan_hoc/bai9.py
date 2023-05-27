arr = []
def tong(n):
    k = 0
    for i in n:
        k += int(i)
    if k < 10:
        return k
    else:
        return tong(str(k))
for i in range(int(input())):
    arr.append(input())
for i in arr:
    print(tong(i))
