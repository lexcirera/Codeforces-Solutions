# https://codeforces.com/problemset/problem/1353/B

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if b[i] > a[i]:
            a[i], b[i] = b[i], a[i]
    print(sum(a))
