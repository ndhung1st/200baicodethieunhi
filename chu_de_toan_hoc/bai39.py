x1, y1, x2, y2 = map(int, input().split())
if x1**2 - x2**2 != y1**2 - y2**2 and x1 != x2 and y1 != y2:
    print(-1)
elif x1 == x2 or y1 == y2:
    canh = max(abs(x1 - x2), abs(y1 - y2))
    if x1 == x2:
        if x2 + canh <= 1000:
            x3 = x2 + canh
        elif x2 - canh >= -1000:
            x3 = x2 - canh
        y3 = y2
        x4 = x3
        y4 = y1
    else:
        if y2 + canh <= 1000:
            y3 = y2 + canh
        elif y2 - canh >= -1000:
            y3 = y2 - canh
        x3 = x2
        y4 = y3
        x4 = x1
    print(x3, y3, x4, y4)
else:
    if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
        x3 = min(x1, x2)
        x4 = max(x1, x2)
        y3 = max(y1, y2)
        y4 = min(y1, y2)
    else:
        x3 = max(x1, x2)
        x4 = min(x1, x2)
        y3 = min(y1, y2)
        y3 = max(y1, y2)
    print(x3, y3, x4, y4)