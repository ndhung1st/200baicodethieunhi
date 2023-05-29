n, m = map(int, input().split())
a = list(map(int, input().split()))
stt = [int(i) for i in range(1, n + 1)]     
while len(stt) > 1:
    if a[0] - m <= 0:                       
        a.pop(0)                           
        stt.pop(0)
    else:                                   
        a.append(a[0] - m)                  
        a.pop(0)                            
        stt.append(stt[0])
        stt.pop(0)        
print(stt[0])