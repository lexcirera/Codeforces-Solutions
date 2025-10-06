# https://codeforces.com/problemset/problem/59/A

s = input()
upper = sum(1 for c in s if c.isupper())
lower = len(s) - upper
print(s.lower() if lower >= upper else s.upper())
