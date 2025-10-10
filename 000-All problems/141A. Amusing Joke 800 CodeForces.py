# https://codeforces.com/problemset/problem/141/A

a = input()
b = input()
c = input()
print("YES" if sorted(a + b) == sorted(c) else "NO")
