from math import log2           
def nhom(k):                    # chia dãy thành các nhóm (4 7) (44 47 74 77) (444 447 474 477 744 747 774 777)
    nh = log2(k/2 + 1)          # số phần tử của nhóm n là 2^n phần tử nên ta dễ ràng suy ra được nhóm của số k (giải bằng toán học)
    if int(nh) < nh:
        return int(nh + 1)
    return nh // 1

arr = []
for i in range(int(input())):
    arr.append(int(input()))
for i in arr:
    stt = i - 2**nhom(i) + 2            # tính được số thứ tự của số k trong nhóm
    sopt = 2**nhom(i)                   # tính được số phần tử của nhóm chứa k
    so = ''
    while sopt > 1:                     # nhận xét thấy nếu chia nhóm thành 2 phần thì phần bên trái sẽ có số 4 xếp trước, phần còn lại là số 7 xếp trước
        if stt <= sopt // 2:            # nếu số k nằm ở phần bên trái ta chọn số 4
            so += '4'                   
            sopt //=2                   # và chia đôi nhóm 
        else:
            so += '7'
            stt -= sopt//2              # trường hợp này k nằm ở phía bên phải nên phải làm mới số thứ tự của k (trong nhóm mới)
            sopt //= 2
    print(so)