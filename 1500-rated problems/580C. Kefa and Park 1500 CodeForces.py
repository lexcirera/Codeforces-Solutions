# https://codeforces.com/problemset/problem/580/C

n, m = map(int,input().split())
a = list(map(int,input().split()))
g = [[] for _ in range(n)]
for _ in range(n-1):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

res = 0
stack = [(0, -1, a[0])]
while stack:
    u, p, cats = stack.pop()
    if cats>m:
        continue
    leaf = True
    for v in g[u]:
        if v == p:
            continue
        leaf = False
        stack.append((v, u, cats+1 if a[v] else 0))
    if leaf:
        res += 1
print(res)

