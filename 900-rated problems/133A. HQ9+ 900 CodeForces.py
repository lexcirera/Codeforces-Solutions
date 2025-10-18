# https://codeforces.com/problemset/problem/133/A

p = input()
print("YES" if any(c in "HQ9" for c in p) else "NO")
