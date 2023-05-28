arr = []
for i in range(int(input())):
    arr.append(input())
for i in arr:
    l, r, a, b = map(int, i.split())
    boia1 = (l + a - 1) // a * a
    if (r + a - 1) // a * a > r:
        boia2 = (r + a - 1) // a * a - a
    else:
        boia2 = (r + a - 1) // a * a
    boib1 = (l + b - 1) // b * b
    if (r + b - 1) // b * b > r:
        boib2 = (r + b - 1) // b * b - b
    else:
        boib2 = (r + b - 1) // b * b
    print((boia2 - boia1)//a + (boib2 - boib1)//b + 2)