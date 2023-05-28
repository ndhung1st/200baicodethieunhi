def tong(n):
    t = 0
    for i in str(n):
        t += int(i)
    return t
k = int(input())
shh = 10
while k > 0:
    if tong(shh + 9) == 10:
        k -= 1
    shh += 9
print(shh)
