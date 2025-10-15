# https://codeforces.com/problemset/problem/1360/B

t = int(input())
for _ in range(t):
    n = int(input())
    s = sorted(map(int,input().split()))
    print(min(s[i+1]-s[i] for i in range(n-1)))
