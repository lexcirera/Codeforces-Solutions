# https://codeforces.com/problemset/problem/1985/B

t = int(input())
for _ in range(t):
    n = int(input())
    bx, bv = 2, 0
    for x in range(2,n+1):
        k = n//x
        v = x*k*(k+1)//2
        if v > bv:
            bv = v
            bx = x
    print(bx)
