arr = []
for i in range(int(input())):
    n = int(input())
    arr.append(n*(n - 1))           # mỗi người cần gửi (N - 1) tin
for i in arr:                       # N người cần gửi N*(N - 1) tin
    print(i)