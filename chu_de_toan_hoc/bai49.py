n, k = map(int, input().split())
a = int('1' + '1'*k)                # k = 1 -> sum = N + 10N = 11N
print(n * a)                        # k = 2 -> sum = N + 10N + 100N = 111N
                                    # k = x -> sum = (111..1)N  (có x số 1)