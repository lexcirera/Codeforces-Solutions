# https://codeforces.com/problemset/problem/1883/B

from collections import Counter

for _ in range(int(input())):
    n, k = map(int,input().split())
    s = input().strip()
    c = Counter(s)
    odd = sum(v%2 for v in c.values())
    print("YES" if k>=odd-1 else "NO")
