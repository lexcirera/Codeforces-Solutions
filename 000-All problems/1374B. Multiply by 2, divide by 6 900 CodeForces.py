# https://codeforces.com/problemset/problem/1374/B

for _ in range(int(input())):
    n = int(input())
    c2, c3 = 0, 0
    while n%2 == 0:
        n //= 2
        c2 += 1
    while n%3 == 0:
        n //= 3
        c3 += 1
    print(-1 if n!=1 or c2>c3 else c3*2-c2)
