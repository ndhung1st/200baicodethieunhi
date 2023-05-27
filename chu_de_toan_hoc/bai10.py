def phantich(m, p):                                     # N! = 1*2*...*(N - 1)*N 
    k = 0                                               # phân tích các bội của p mà < N thành p^x * (số k)
    while m % p == 0:
        k += 1
        m //= p
    return k

arr = []
for i in range(int(input())):
    arr.append(input())
for i in arr:
    n, p = map(int, i.split())
    k = 0
    for i in range(p, int(n / p) * p + 1, p):
        k += phantich(i, p)                             # cộng các mũ vào với nhau
    print(k)