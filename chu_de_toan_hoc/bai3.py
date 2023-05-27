arr = []
for i in range(int(input())):
    n,x = map(int, input().split())
    arr.append((10 - x)*(n - 1))        # tổng thời gian khám bệnh cho N - 1 người = 10*(N - 1) + X (phút) (cộng thêm thời gian đợi người đầu tiên)
for i in arr:                           # thời gian từ lúc đầu đên lúc người thứ N đên = N*X (phút)
    print(i)                            # thời gian người thứ N cần đợi là 10*(N - 1) + X - N*X = (10 - X)*(N - 1) (phút)