# https://codeforces.com/problemset/problem/1901/A

t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    a = [0]+a+[x]
    d = []
    for i in range(1, len(a)):
        d.append(a[i]-a[i-1])
    d.append(2*(x-a[-2]))
    print(max(d))
