a = int(input())
b = 0                           
if '8' not in str(a):                   
    while '8' not in str(a):
        b += 1
        a += 1
else:
    if a % 10 != 8:
        while a % 10 != 8:
            b += 1
            a += 1
    else:
        a += 1
        b += 1
        while a % 10 != 8:
            b += 1
            a += 1
print(b)