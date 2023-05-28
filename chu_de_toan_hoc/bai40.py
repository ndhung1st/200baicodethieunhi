n = int(input())
vang = list(map(int, input().split()))
if sum(vang) % 2 == 1 and n == 1:       # nếun chỉ có 1 túi lẻ thì tiền = 0
    print(0)
elif sum(vang) % 2 == 0:                # tổng vàng chẵn -> lấy hết
    print(sum(vang))
else:                                                    
    le = sorted([i for i in vang if i % 2 == 1])        # chia thành 2 loại chẵn và lẻ
    print(sum(vang) - min(le))                          # lây hết vàng chẵn
                                                        # vì tổng lẻ nên phải bớt 1 túi vàng lẻ(bỏ túi ít nhất)