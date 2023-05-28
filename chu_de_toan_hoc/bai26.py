n, k = map(int, input().split())
vuon = [1]*n                            # tạo mảng vuon chứa n phần tử là trạng thái của các mảnh vườn(1: chưa tưới, 0: đã tưới)
voi = list(map(int, input().split()))   
for i in range(k):                      # vì chỉ số của kiểu list bắt đầu từ 0 nên vị trí của các vòi và vườn giảm đi 1
    voi[i] -= 1
for i in voi:                           # các mảnh vường có vòi trong giây đầu tiên sẽ được tưới trước
    vuon[i] = 0
thoigian = 1
vuonp = vuon.copy()                     # tạo mảng vuonp lưu trạng thái cũ cua vuon
while 1 in vuon:                        # các vườn đã được tưới có thể coi là có gắn vòi
    for i in range(n):
        if vuonp[i] == 0:               # vòng lặp để sửa trạng thái của các vườn bên cạnh các vườn có vòi
            if i == 0:
                vuon[1] = 0
            elif i == n - 1:
                vuon[-2] = 0
            else:
                vuon[i + 1] = 0
                vuon[i - 1] = 0
    vuonp = vuon.copy()                 # cập nhật lại giá trị của vuonp
    thoigian += 1                       
print(thoigian)