a, b, s = map(int, input().split())     
if a == 0 and b == 0 and s == 2:        
    print("Yes")
else:
    if abs(a) + abs(b) == s:
        print('Yes')
    else:
        print('No')                     