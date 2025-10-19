# https://codeforces.com/problemset/problem/1850/B

for _ in range(int(input())):
    n = int(input())
    idx, q = 0, 0
    for i in range(1, n+1):
        a, b = map(int,input().split())
        if a <= 10 and b > q:
            q = b
            idx = i
    print(idx)
