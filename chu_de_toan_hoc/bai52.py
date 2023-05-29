a, b, r = map(int, input().split())
s = a * b
if 4 * (r ** 2) > s:
    print("Second")
else:
    print("Frist")