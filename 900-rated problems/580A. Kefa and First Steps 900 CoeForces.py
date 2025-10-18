# https://codeforces.com/problemset/problem/580/A

n = int(input())
a = list(map(int,input().split()))
ans, curr = 1, 1
for i in range(1, n):
    if a[i] >= a[i-1]:
        curr += 1
        ans = max(ans, curr)
    else:
        curr = 1
print(ans)
