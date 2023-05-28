n, k = map(int, input().split())
soi = list(map(int, input().split()))       # sắp xếp các loại sỏi theo thứ tự tăng dần
ngay = 0
soi.sort()
while len(soi) > 1:                         # lặp đến khi chỉ còn 1 loại sỏi (gọi tắt sỏi = s)
    if soi[0] > 2*k:                        # nếu s1 > 2k tức là chỉ nhặt được 1 loại trong 1 ngày và s1 còn dư
        soi[0] -= 2*k                       # s1 còn lại = s1 - 2k
    elif soi[0] > k and soi[0] <= 2*k:      # nếu k < s1 < 2k thì s1 đã hết và chỉ nhặt được 1 loại 1 ngày
        soi.pop(0)                          # xóa s1 khỏi danh sách (lúc này s1 thành s1 và s3 thành s2)
    else:                                   # nếu s1 < k -> vẫn còn 1 túi trống
        if soi[1] > k:                      # nếu s2 > k thì s2 = s2 - k
            soi[1] -= k
            soi.pop(0)                      # xóa s1 khỏi danh sách
        else:
            soi.pop(1)                      # nếu cả s1 và s2 < k
            soi.pop(0)                      # => xóa s1 và s2 khỏi danh sách (s3 thành s1 và s4 thành s2)
    ngay += 1                               # mỗi lần lặp là 1 ngày

soi = soi[0]                                # kết thúc lặp chỉ còn lai 1 loại sỏi
ngay += soi//(2*k) + 1                      # dễ dàng tính được thời gian còn lại

print(ngay)