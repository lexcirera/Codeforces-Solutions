# https://codeforces.com/problemset/problem/1462/A

for _ in range(int(input())):
    n = int(input())
    b = list(map(int,input().split()))
    l, r = 0, n-1
    a = []
    while l <= r:
        a.append(b[l])
        l += 1
        if l <= r:
            a.append(b[r])
            r -= 1
    print(*a)
