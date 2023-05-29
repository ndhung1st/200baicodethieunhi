def giaipt(k):
    d = 1 - 4*k
    if d < 0:
        return False
    if int((-1 - d**(1/2)) / 2) == (-1 - d**(1/2)) / 2 and (-1 - d**(1/2)) / 2 >= 1:
        return True
    if int((-1 + d**(1/2)) / 2) == (-1 + d**(1/2)) / 2 and (-1 + d**(1/2)) / 2 >= 1:
        return True
    return False
t = int(input())
n = []
for i in range(t):
    n.append(int(input()))
for i in range(t):
    a = 1
    kt = True
    while a < (-1 + (1 + 4*n[i])**(1/2))/2:
        k = a*(a + 1) - 2*n[i]
        if giaipt(k):
            print("Yes")
            kt = False
            break
        a += 1
    if kt:
        print("No")