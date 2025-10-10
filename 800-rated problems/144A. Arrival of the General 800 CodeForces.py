# https://codeforces.com/problemset/problem/144/A

n = int(input())
a = list(map(int, input().split()))
x = a.index(max(a))
y = len(a) - 1 - a[::-1].index(min(a))
print(x + (n - 1 - y) - (y < x))
