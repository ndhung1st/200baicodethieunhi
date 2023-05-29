a, b = map(int, input().split())
if a == b:
    print(str(a)[::-1])
elif a // b >= 10:
    print(str(a)[::-1])
elif b // a > 10:
    print(str(b)[::-1])
else:
    while True:
        if a % 10 > b % 10:
            print(str(a)[::-1])
            break
        elif b % 10 > a % 10:
            print(str(b)[::-1])
            break
        a //= 10
        b //= 10