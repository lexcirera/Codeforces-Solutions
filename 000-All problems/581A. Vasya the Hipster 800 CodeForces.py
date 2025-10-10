# https://codeforces.com/problemset/problem/581/A

a, b = map(int, input().split())
x = min(a, b)
y = (max(a, b) - x) // 2
print(x, y)
