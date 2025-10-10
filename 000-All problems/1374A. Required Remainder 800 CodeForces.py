# https://codeforces.com/problemset/problem/1374/A

t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    print(n - (n - y) % x)
