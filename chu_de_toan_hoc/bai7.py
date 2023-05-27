arr = []
def tim(a,b):
    l = []
    for i in range(len(a)):
        if (a[i] - b[i]) >= 0:
            l.append(a[i] - b[i])
        else:
            l.append((a[i] - b[i]) * -1)
    return max(l)
for i in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    arr.append(tim(a,b))
print(max(arr))