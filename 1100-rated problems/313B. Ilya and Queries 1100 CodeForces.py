# https://codeforces.com/problemset/problem/313/B

s = input().strip()
n = len(s)
p = [0]*n
for i in range(1, n):
    p[i] = p[i-1]+(s[i]==s[i-1])
m = int(input())
for _ in range(m):
    l, r = map(int,input().split())
    print(p[r-1]-p[l-1])
