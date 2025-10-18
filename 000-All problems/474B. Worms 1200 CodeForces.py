# https://codeforces.com/problemset/problem/474/B

import bisect
n = int(input())
a = list(map(int,input().split()))
p = []
s = 0
for x in a:
    s += x
    p.append(s)
m = int(input())
q = list(map(int,input().split()))
for x in q:
    print(bisect.bisect_left(p, x)+1)