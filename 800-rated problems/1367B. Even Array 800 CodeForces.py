# https://codeforces.com/problemset/problem/1367/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c0, c1 = 0, 0
    for i in range(n):
        if a[i]%2 != i%2:
            if i%2 == 0:
                c0 += 1
            else:
                c1 += 1
    print(c0 if c0 == c1 else -1)
