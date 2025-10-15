# https://codeforces.com/problemset/problem/1374/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    bal = 0
    mn = 0
    for ch in s:
        bal += 1 if ch == '(' else -1
        mn = min(mn, bal)
    print(-mn)
