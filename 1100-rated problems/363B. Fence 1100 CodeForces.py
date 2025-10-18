# https://codeforces.com/problemset/problem/363/B

n, k = map(int,input().split())
h = list(map(int,input().split()))
s = sum(h[:k])
mn = s
idx = 0
for i in range(k,n):
    s += h[i]-h[i-k]
    if s < mn:
        mn = s
        idx = i-k+1
print(idx+1)
