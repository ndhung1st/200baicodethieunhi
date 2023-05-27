def tinh(n):
    if n % 2 == 0:                  # dễ dàng tính được max(a) = n/2 - 1 (n chẵn) or max(a) = n//2 (n lẻ)
        k = n//2 - 1                # với a = 1  => min(b) = (1 + 1), max(b) = (n - 1) => số cách chọn = (n - 1) - (1 + 1) + 1 = n - 2
    else:                           # với a = 2  => min(b) = (2 + 1), max(b) = (n - 2) => số cách chọn = (n - 2) - (1 + 2) + 1 = n - 4
        k = n//2                    # với a = k  => min(b) = (k + 1), max(b) = (n - k) => số cách chọn = (n - k) - (1 + k) + 1 = n - 2k
    return k * (n - k - 1)          # tổng cách chọn = n*k -2-4-6-...-2k = k*(n - k - 1) cách

arr = []
for i in range(int(input())):
    arr.append(int(input()))
for i in arr:
    print(tinh(i))