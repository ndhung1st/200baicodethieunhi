n, m, a, b = map(int, input().split())
if 1 / a >= m / b:                       # xem chon vé đặc biệt có bị lỗ không
    print(n * a)                         # nếu lỗ -> dùng tất vé thường
else:
    tien = (n // m) * b + (n % m) * a    # nêu không thì dùng tối đa vé đặc biệt có thể dùng + vé thường
print(tien)