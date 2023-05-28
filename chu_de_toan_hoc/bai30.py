n = int(input())
doi = []
for i in range(n):
    k = list(map(int, input().split())) 
    doi.append(k[1])
giay = 0
i = 0
while i < n:
    if doi[i] > giay:               
        giay += 1
        i += 1
        print(giay, end = ' ')
    else:
        print(0, end = ' ')
        i += 1
