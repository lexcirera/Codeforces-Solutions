# https://codeforces.com/problemset/problem/1772/A

t = int(input())
for _ in range(t):
    s = input().strip()
    a, b = map(int,s.split('+'))
    print(a+b)
