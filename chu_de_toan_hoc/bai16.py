n, a, b = map(int, input().split())
def sua(s, a, b):
    while a * b < s:
        if s % a == 0 and s // a > b:       # min(a, b) là ước của 6*n và s // min(a, b) > max(a, b)
            b = s // a                      # => a1 * b1 = s với a1(or b1) = min(a, b) và b1(or a1) = s // min(a, b)
            return [a * b, a, b]
        elif s % b == 0 and s // b > a:
            a = s // b
            return [a * b, a, b]
        if a < b:                           # nếu không số nào là ước thì tăng số bé lên 1 đơn vị để min(a, b) -> ước nào đó của 6*n
            a += 1
        else:
            b += 1
    return [a * b, a, b]
if a * b >= 6 * n:                          
    print(a * b)
    print(a, b)
else:
    s, a1, b1 = sua(n*6, a, b)
    print(s, '\n', a1,' ', b1, sep='')