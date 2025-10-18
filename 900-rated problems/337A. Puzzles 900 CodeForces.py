# https://codeforces.com/problemset/problem/337/A

n, m = map(int, input().split())
f = sorted(map(int, input().split()))
print(min(f[i+n-1]-f[i] for i in range(m-n+1)))
