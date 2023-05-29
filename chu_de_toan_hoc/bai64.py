n = int(int(input()))
a = sorted(list(map(int, input().split())))
lan = 0
nhom = [0,0,0,0,0]
for i in a:
    nhom[i] += 1
lan += nhom[4]
lan += nhom[2] // 2 
nhom[2] %= 2
if nhom[1] > nhom[3]:
    lan += nhom[3]
    nhom[1] -= nhom[3]
    if nhom[2] == 1:
        lan += 1
        nhom[1] -= 2
    if nhom[1] % 4 == 0 and nhom[1] > 0:
        lan += nhom[1] // 4 
    else:
        lan += nhom[1] // 4 + 1
else:
    lan += nhom[1]
    nhom[3] -= nhom[1]
    lan += nhom[3] + nhom[2]
print(lan)