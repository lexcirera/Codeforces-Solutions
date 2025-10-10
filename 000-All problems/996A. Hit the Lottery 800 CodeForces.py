# https://codeforces.com/problemset/problem/996/A

n = int(input())
res = 0
for x in [100, 20, 10, 5, 1]:
    res += n // x
    n %= x
print(res)
