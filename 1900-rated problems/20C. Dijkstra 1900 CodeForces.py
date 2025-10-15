# https://codeforces.com/problemset/problem/20/C

import heapq

# ---------- input ----------
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))# undirected

# ---------- Dijkstra ----------
dist   = [float('inf')] * (n + 1)
parent = [-1]  * (n + 1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue
    if u == n:
        break
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            parent[v] = u
            heapq.heappush(pq, (nd, v))

# ---------- output ----------
if dist[n] == float('inf'):
    print(-1)
else:
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    print(*reversed(path))