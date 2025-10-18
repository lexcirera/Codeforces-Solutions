# https://codeforces.com/problemset/problem/230/B

n = int(input())
a = list(map(int,input().split()))
lim = int(1e6)+1
p = [1]*lim
p[0], p[1] = 0, 0
for i in range(2,int(lim**0.5)+1):
    if p[i]:
        for j in range(i**2, lim, i):
            p[j] = 0
s = {i**2 for i in range(2, lim) if p[i]}
for x in a:
    print("YES" if x in s else "NO")
