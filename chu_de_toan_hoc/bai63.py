n = int(input())
print(int((n**3)/6 + (n**2)/2 + n/3))       # một tháp là một phần tử trong dãy U(n): n*(n + 1)/2
                                            # công thức truy hôi của U(n): u(1) = 1
                                            #                              U(n+1) = U(n) + n + 1
                                            # giả sử số viên gạch cần để xây n tháp là phần tử của dãy K(n)
                                            # -> công thức truy hồi của K(n): k(1) = 1
                                            #                                 K(n + 1) = k(n) + u(n+1) = k(n) + u(n) + n + 1
                                            #                                          = k(n) + n^2/2 + 3n/2 + 1
                                            # dùng các phép biến đổi toán học tìm được k(n) = n^3/6 + n^2/2 + n/3