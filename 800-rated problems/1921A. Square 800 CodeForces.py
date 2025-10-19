# https://codeforces.com/problemset/problem/1921/A

t = int(input())
for _ in range(t):
    xs, ys = [], []
    for _ in range(4):
        x, y = map(int,input().split())
        xs.append(x)
        ys.append(y)
    d = max(max(xs)-min(xs), max(ys)-min(ys))
    print(d**2)
