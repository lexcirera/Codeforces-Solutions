# https://codeforces.com/problemset/problem/489/B

n = int(input())
a = sorted(map(int,input().split()))
m = int(input())
b = sorted(map(int,input().split()))
i, j, ans = 0, 0, 0
while i<n and j<m:
    if abs(a[i]-b[j])<=1:
        ans += 1
        i += 1
        j += 1
    elif a[i]<b[j]:
        i += 1
    else:
        j += 1
print(ans)
