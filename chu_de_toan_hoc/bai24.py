from math import log                # dãy số biểu thị cân nặng của BearA và BearB lần lượt là:
a, b = map(int, input().split())    # A(n) = a.3^(n - 1)  (với a là cân nặng năm đầu tiên, n là năm thứ n)
n = log(a/b, 2/3) + 1               # B(n) = b.2^(n - 1)  (với b là cân nặng năm đầu tiên, n là năm thứ n) -> thời gian  cần tìm là (n - 1) năm
print(int(n))                       # ta có pt A(n) > B(n) <=> a/b > (2/3)^(n - 1)
                                    # => log2/3(a/b) < n - 1
                                    # <=> n > log2/3(a/b) + 1 (với n nguyên và nhỏ nhất)