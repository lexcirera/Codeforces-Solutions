# https://codeforces.com/problemset/problem/1915/C

import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    x = int(math.isqrt(s))
    print("YES" if x**2==s else "NO")
