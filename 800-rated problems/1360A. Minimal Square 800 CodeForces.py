# https://codeforces.com/problemset/problem/1360/A

t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    print(max(2*min(a, b), max(a, b))**2)
