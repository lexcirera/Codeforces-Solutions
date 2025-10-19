# https://codeforces.com/problemset/problem/368/B

n, m = map(int,input().split())
a = list(map(int,input().split()))
suffix = [0]*(n+1)
seen = set()
for i in range(n-1,-1,-1):
    seen.add(a[i])
    suffix[i] = len(seen)
for _ in range(m):
    l = int(input())-1
    print(suffix[l])
