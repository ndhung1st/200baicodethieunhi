tong_sach = sum([int(i) for i in input().split()])
tong_vo = sum([int(i) for i in input().split()])
n = int(input())
if tong_sach % 5 == 0:
    n -= tong_sach // 5
else:
    n -= tong_sach // 5 + 1
if tong_vo % 10 == 0:
    n -= tong_vo // 10
else:
    n -= tong_vo // 10 + 1
if n >= 0:
    print('Yes')
else:
    print("No")