# https://codeforces.com/problemset/problem/456/A

n = int(input())
a = [tuple(map(int,input().split())) for _ in range(n)]
a.sort()
print("Happy Alex" if any(a[i][1]>a[i+1][1] for i in range(n-1)) else "Poor Alex")
