# https://codeforces.com/problemset/problem/327/A

n = int(input())
a = list(map(int,input().split()))
s = sum(a)
b = [1 if x==0 else -1 for x in a]
mx, c = b[0],b[0]
for x in b[1:]:
    c = max(x,c+x)
    mx = max(mx,c)
print(s-1 if s==n else s+mx)
