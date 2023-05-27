def kt(a):
    x = (((1+8*a)**(1/2)) - 1)/2            # các số tam giác thuôc dãy (un) = n*(n + 1)/2
    if x//1 == x:                           # ==> nếu pt n*(n + 1)/2 = a <=> n^2 + n - 2a = 0 có nghiệm nguyên dương thì a là số tam giác
        print(1)
    else:
        print(0)
arr = []
for i in range(int(input())):
    arr.append(int(input()))
for i in arr:
    kt(i)