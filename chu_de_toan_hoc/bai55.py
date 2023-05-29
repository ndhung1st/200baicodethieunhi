so = sorted(list(map(int, input().split())))
if so[0] + so[2] == 2*so[1]:
    print(so[2]*2 - so[1])
else:
    d = min(so[1] - so[0], so[2] - so[1])
    if so[2] - so[1] == d:
        print((so[0] + so[1]) // 2)
    else:
        print((so[1] + so[2]) // 2)