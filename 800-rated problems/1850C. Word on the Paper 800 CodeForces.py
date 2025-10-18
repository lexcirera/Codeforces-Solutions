# https://codeforces.com/problemset/problem/1850/C

for _ in range(int(input())):
    g = [input().strip() for _ in range(8)]
    for j in range(8):
        s = ''
        for i in range(8):
            if g[i][j] != '.':
                s += g[i][j]
        if s:
            print(s)
            break
