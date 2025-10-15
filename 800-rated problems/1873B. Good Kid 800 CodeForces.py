# https://codeforces.com/problemset/problem/1873/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    a[0] += 1
    p = 1
    for x in a:
        p *= x
    print(p)
