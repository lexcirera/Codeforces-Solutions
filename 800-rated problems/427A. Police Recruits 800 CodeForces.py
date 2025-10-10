# https://codeforces.com/problemset/problem/427/A

n = int(input())
arr = list(map(int, input().split()))
p = 0
u = 0
for x in arr:
    if x == -1:
        if p > 0:
            p -= 1
        else:
            u += 1
    else:
        p += x
print(u)
