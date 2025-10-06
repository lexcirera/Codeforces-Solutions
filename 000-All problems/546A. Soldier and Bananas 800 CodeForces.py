# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())
tot = k * w * (w + 1) // 2
print(max(0, tot - n))
