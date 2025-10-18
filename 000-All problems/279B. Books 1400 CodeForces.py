# https://codeforces.com/problemset/problem/279/B

n, t = map(int,input().split())
a = list(map(int,input().split()))
l, s, ans = 0, 0, 0
for r in range(n):
    s += a[r]
    while s > t:
        s -= a[l]
        l += 1
    ans = max(ans, r-l+1)
print(ans)
