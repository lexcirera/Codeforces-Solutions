# https://codeforces.com/problemset/problem/460/A

n, m = map(int,input().split())
d = 0
while n > 0:
    d += 1
    n -= 1
    if d%m == 0:
        n += 1
print(d)
