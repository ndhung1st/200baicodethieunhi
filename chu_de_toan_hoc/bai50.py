n = input()
tong = 0
for i in range(4):
    tong += int(n[i])
if int(tong ** (1/2)) ** 2 == tong:
    print("Yes")
else:
    print("No")