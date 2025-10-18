# https://codeforces.com/problemset/problem/706/B

import bisect
n = int(input())
x = sorted(map(int,input().split()))
q = int(input())
for _ in range(q):
    m = int(input())
    print(bisect.bisect_right(x, m))
