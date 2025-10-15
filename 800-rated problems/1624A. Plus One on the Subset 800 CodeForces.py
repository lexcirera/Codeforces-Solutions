# https://codeforces.com/problemset/problem/1624/A

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(max(a)-min(a))
