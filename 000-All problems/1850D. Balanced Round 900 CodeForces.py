# https://codeforces.com/problemset/problem/1850/D

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = sorted(map(int,input().split()))
    mx, curr = 1, 1
    for i in range(1,n):
        if a[i]-a[i-1]<=k:
            curr += 1
        else:
            curr = 1
        mx = max(mx, curr)
    print(n-mx)
