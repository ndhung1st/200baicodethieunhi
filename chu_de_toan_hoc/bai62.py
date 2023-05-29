a, b, c = map(int, input().split())
vo = a + b
chai = 0
while vo >= c:
    chai += vo // c
    vo = vo % c + vo // c
print(chai)