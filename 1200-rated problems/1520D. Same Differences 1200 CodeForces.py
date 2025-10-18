# https://codeforces.com/problemset/problem/1520/D

from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    c = Counter()
    res = 0
    for i, x in enumerate(a):
        res+=c[x-i]
        c[x-i] += 1
    print(res)
