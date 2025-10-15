# https://codeforces.com/problemset/problem/1873/C

t = int(input())
for _ in range(t):
    g = [input().strip() for _ in range(10)]
    s = 0
    for i in range(10):
        for j in range(10):
            if g[i][j] == 'X':
                r = min(i, j, 9-i, 9-j)+1
                s += r
    print(s)
