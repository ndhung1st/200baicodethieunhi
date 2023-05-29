a, b = map(str, input().split())
amax = bmax = amin = bmin = ''
for i in a:
    if i == "5" or i == '6':
        amax += '6'
        amin += '5'
    else:
        amax += i
        amin += i
for i in b:
    if i == "5" or i == '6':
        bmax += '6'
        bmin += '5'
    else:
        bmax += i
        bmin += i
print(int(amin) + int(bmin), int(amax) + int(bmax))