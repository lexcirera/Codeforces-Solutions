# https://codeforces.com/problemset/problem/1676/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = min(a)
    print(sum(x-m for x in a))
