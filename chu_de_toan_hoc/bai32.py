a, b, c = map(int, input().split())
y = 0
kt = False
while y <= c / b:
    x = (c - b*y) / a
    if int(x) == x:
        x = int(x)          # giống bài 28
        kt = True
        break
    y += 1
if kt == True:
    print("Yes")
else:
    print("No")