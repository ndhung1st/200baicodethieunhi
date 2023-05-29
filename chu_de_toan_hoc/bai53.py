n, k = map(int, input().split())
if k // n > 2:          
    print(0)
else:
    print(n - k % 4)