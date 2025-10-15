# https://codeforces.com/problemset/problem/492/A

n = int(input())
h, s = 0, 0
while n >= s+h+1:
    h += 1
    s += h
    n -= s
print(h)
