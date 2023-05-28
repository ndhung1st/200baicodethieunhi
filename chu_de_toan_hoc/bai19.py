n, m = map(int, input().split())
def tinh(n, m):                             # số bước <= n
    if n < m:                               # không tồn tại bội của m < m
        return -1
    buoc = n // 2 + n % 2                   # giả sử số bước là nhỏ nhất(nhiều lần bước 2 nhất)
    while buoc % m != 0 and buoc <= n:      
        buoc += 1                           # nếu số bước không phải bội của m thì tách bước 2 thành {1,1} (vd {2, 2, 1} -> {2, 1, 1, 1})
    if buoc % m != 0:
        return -1                           # return về đáp án
    return buoc
print(tinh(n, m))