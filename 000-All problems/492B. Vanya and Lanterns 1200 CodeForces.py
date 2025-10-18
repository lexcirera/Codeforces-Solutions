# https://codeforces.com/problemset/problem/492/B

n, l = map(int, input().split())
a = sorted(map(int,input().split()))
mx = max(a[0], l-a[-1])
for i in range(1, n):
    mx = max(mx, (a[i]-a[i-1])/2)
print(f"{mx:.10f}")
