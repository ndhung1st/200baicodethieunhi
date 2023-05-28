n, a, b, c = map(int, input().split())
if a < b - c:                       # nếu tổng tiền mất khi mua lọ thủy tinh(đã trả lọ) > tiền mua hộp 
    print(n // a)                   # mua tất cả hộp -> số hộp mua đc  -> n // a
else:
    sua = (n - b) / (b - c) + 1     # trường hợp còn lại
    if int(sua) == sua:             # số tiền sau mỗi lần mua lọ thủy tinh rồi bán lại tuân theo quy tắc của dãy:
        print(int(sua))             # U(1) = n
    else:                           # U(k + 1) = U(k) - b + c (cấp số cộng) -> U(k) = n + (k - 1)*(c - b)
        print(int(sua + 1))         # để mua được lọ thủy tinh -> U(k) > b
                                    # -> k >= (n - b)/(b - c) + 1  (k nguyên) (k chính là số lọ mua được)