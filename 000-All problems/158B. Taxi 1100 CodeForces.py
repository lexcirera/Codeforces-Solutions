# https://codeforces.com/problemset/problem/158/B

n = int(input())
a = list(map(int,input().split()))
c = [0]*5
for x in a:
    c[x] += 1
res = c[4]+c[3]+(c[2]//2)
c[1] = max(0, c[1]-c[3])
if c[2]%2:
    res += 1
    c[1] = max(0, c[1]-2)
res += (c[1]+3)//4
print(res)
