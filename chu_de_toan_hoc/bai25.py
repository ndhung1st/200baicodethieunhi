x, y = map(int, input().split())                      # lần chụp đầu -> 2 màu 1 đen trắng
if y - 1 <= x:                                        # lần tiếp theo: +TH1: chụp màu-> ảnh màu(lẻ),  đen trắng(chẵn)
    if (y % 2 == 0 and x % 2 == 1) or (y % 2 == 1 and x % 2 == 0):    #+TH2: chụp đen trắng -> ảnh màu(chẵn), đen trắng(lẻ)
        print('Yes')                                  # nhận xét: nếu ảnh này lẻ thì ảnh kia chẵn và số ảnh màu <= đen trắng - 1
    else:
        print('No')
else:
    print('No')