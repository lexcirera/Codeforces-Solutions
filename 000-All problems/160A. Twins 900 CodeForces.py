# https://codeforces.com/problemset/problem/160/A

n = int(input())
a = sorted(map(int,input().split()), reverse=True)
s = sum(a)
curr = 0
for i,x in enumerate(a,1):
    curr+=x
    if curr>s-curr:
        print(i)
        break
