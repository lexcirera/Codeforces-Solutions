# https://codeforces.com/problemset/problem/731/A

s = input().strip()
curr = 'a'
res = 0
for c in s:
    d = abs(ord(c)-ord(curr))
    res += min(d,26-d)
    curr = c
print(res)
