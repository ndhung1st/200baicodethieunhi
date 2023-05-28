x = int(input())
hh, mm = map(int, input().split())
def dongho(x, hh, mm):
    while '7' not in str(hh) and '7' not in str(mm):
        if mm - x < 0:
            mm = 60 - x + mm
            if hh == 0:
                hh = 23
            else:
                hh -= 1
        else:
            mm -= x
    return [hh, mm]
a = dongho(x, hh, mm)
gio = a[0]
phut = a[1]
if hh >= gio:
    print((hh*60 + mm - gio * 60 - phut) // x)
else:
    print(((24 + hh) * 60 + mm - gio * 60 - phut) // x)