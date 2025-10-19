# https://codeforces.com/problemset/problem/233/A

n = int(input())
if n%2:
    print(-1)
else:
    print(*[i+1 if i%2==1 else i-1 for i in range(1,n+1)])
