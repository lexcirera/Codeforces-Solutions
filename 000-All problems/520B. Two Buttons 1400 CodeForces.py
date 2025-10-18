# https://codeforces.com/problemset/problem/520/B

n, m = map(int,input().split())
cnt = 0
while m > n:
    if m%2 == 0:
        m//=2
    else:
        m += 1
    cnt += 1
print(cnt+n-m)
