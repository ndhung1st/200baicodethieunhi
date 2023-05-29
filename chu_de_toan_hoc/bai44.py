n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)  
def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True            
while True:
    if snt(k):
        if k in a:
            print(1)
        else:
            print(k)
    else:
        for i in a:
            if k % i == 0:
                print(i)
                break
    break