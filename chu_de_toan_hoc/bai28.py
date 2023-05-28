n, a, b = map(int, input().split())
y = 0
k = False
while y <= n / b:           # các dữ kiện phải thỏa mãn PT Ax + By = N
    x = (n - b*y) / a       # =>   "x = (N - By)/A"   >= 0 <=>    "y < N/B"
    if int(x) == x:
        x = int(x)
        print('Yes')
        k = True
        break
    y += 1
if k == True:
    print(x, y)
else:
    print('No')