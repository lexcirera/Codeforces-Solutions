# https://codeforces.com/problemset/problem/742/A

n = int(input())
if n == 0:
    print(1)
else:
    print([6, 8, 4, 2][n % 4])
