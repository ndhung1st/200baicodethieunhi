def kt(n):
    k = 0
    for i in n:
        if i == '1':
            k += 1
    if k % 2 == 0:
        print('even')
    else:
        print('odd')
arr = []
for i in range(int(input())):
    arr.append(bin(int(input()))[2::])
for i in arr:
    kt(i)