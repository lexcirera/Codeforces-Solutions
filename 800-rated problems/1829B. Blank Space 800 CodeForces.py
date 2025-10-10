# https://codeforces.com/problemset/problem/1829/B

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = m = 0
    for x in a:
        if x == 0:
            c += 1
            m = max(m, c)
        else:
            c = 0
    print(m)