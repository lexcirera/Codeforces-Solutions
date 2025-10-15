# https://codeforces.com/problemset/problem/131/A

s = input()
print(s.swapcase() if s==s.upper() or (s[0].islower() and s[1:]==s[1:].upper()) else s)
