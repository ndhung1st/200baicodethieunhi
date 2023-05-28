a, b = map(int, input().split())
x, y, z = map(int, input().split())
can  = 0
if a < 2*x + y:
    can += 2*x + y - a
if b < 3*z + y:
    can += 3*z + y - b
print(can)