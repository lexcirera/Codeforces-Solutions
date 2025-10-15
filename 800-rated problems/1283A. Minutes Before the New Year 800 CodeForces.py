# https://codeforces.com/problemset/problem/1283/A

t = int(input())
for _ in range(t):
    h, m =map(int,input().split())
    print((23-h)*60+(60-m))
