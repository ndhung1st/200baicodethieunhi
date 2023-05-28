def hopso(n):
    for i in range(2, int(n ** 1/2) + 1):       # theo định nghĩa -> hợp số không phải là số nguyên tố
        if n % i == 0:                     
            return  True
    return False
n = int(input())
a = 4
while a <= n / 2:
    if hopso(a) and hopso(n - a):
        print(a, n - a)
        break
    a += 1