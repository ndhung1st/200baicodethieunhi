arr = []
for i in range(int(input())):
    arr.append(input())
for i in arr:
    x, y, n = map(int, i.split())
    if n % 2 == 0:                                      # nếu số lượt chơi chẵn => x, y được nhân 1 lượng bằng nhau
        print(int(max(x,y) // min(x,y)))                # => tỉ số = max(x, y) / min (x, y)  (phần được nhân triệt tiêu)
    else:
        print(int(max(x * 2, y) / min(x * 2, y)))       # nếu số lượt chơi lẻ => x nhân đôi hơn y 1 lần
                                                        # => tỉ số = max(2x, y) / min(2x, y)