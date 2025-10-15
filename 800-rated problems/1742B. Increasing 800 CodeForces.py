# https://codeforces.com/problemset/problem/1742/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print("YES" if len(set(a))==n else "NO")
