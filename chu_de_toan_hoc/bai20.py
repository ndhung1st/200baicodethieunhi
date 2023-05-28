x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

print(max(abs(x2 - x1), abs(y2 - y1)))      # tịnh tiến 2 tọa độ theo vecto(-x1, -y1) để (x1, x2) -> (0,0)
                                            # cách đi ngắn nhất là ưu tiên đi chéo -> thẳng
                                            # vẽ trục tọa độ thấy số bước = min(x2, y2) + max(x2, y2) - min(x2, y2)
                                            # = max(x2, y2)