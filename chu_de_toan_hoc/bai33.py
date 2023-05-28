l, r = map(int, input().split())
boi = []
for i in range((l + 13 - 1) // 13 * 13, r + 1, 13):      
    boi.append(i)
tong = (l + r)*(r - l + 1) // 2 - sum(boi)
print(tong)