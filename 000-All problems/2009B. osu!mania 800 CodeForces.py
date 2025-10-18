# https://codeforces.com/problemset/problem/2009/B

for _ in range(int(input())):
    n = int(input())
    g = [input().strip() for _ in range(n)]
    res = []
    for row in reversed(g):
        res.append(row.index('#')+1)
    print(*res)
