xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
xd, yd = map(int, input().split())
ab = ((xa - xb)**2 + (ya - yb)**2)**(1/2)
ac = ((xa - xc)**2 + (ya - yc)**2)**(1/2)
cb = ((xc - xb)**2 + (yc - yb)**2)**(1/2)
da = ((xa - xd)**2 + (ya - yd)**2)**(1/2)
db = ((xd - xb)**2 + (yd - yb)**2)**(1/2)
dc = ((xc - xd)**2 + (yc - yd)**2)**(1/2)
def heron(c1, c2, c3):
    return (c1/2 + c2/2 + c3/2*(c1/2 + c2/2 + c3/2-c1)*(c1/2 + c2/2 + c3/2-c2)*(c1/2 + c2/2 + c3/2-c3))**(1/2)
if heron(ab,ac,cb) - heron(ab, da, db) - heron(ac, da, dc) - heron(cb, dc, db) <= 0.0001:
    print(1)
else:
    print(0)