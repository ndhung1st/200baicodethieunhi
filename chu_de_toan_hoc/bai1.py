def sua(n):
    k = ''
    for i in range(len(n)):
        if n[i] == '0':
            k += '5'
        else:
            k += n[i]
    return k
a = []
for i in range(int(input())):
    a.append(input())
for i in range(len(a)):
    a[i] = sua(a[i])
for i in a:
    print(i)