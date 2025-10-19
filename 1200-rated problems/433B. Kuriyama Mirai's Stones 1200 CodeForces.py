# https://codeforces.com/problemset/problem/433/B

n = int(input())
v = list(map(int,input().split()))
p1 = [0]*(n+1)
for i in range(n):
    p1[i+1] = p1[i]+v[i]
u = sorted(v)
p2 = [0]*(n+1)
for i in range(n):
    p2[i+1] = p2[i]+u[i]
m = int(input())
for _ in range(m):
    t, l, r =map(int,input().split())
    if t == 1:
        print(p1[r]-p1[l-1])
    else:
        print(p2[r]-p2[l-1])
