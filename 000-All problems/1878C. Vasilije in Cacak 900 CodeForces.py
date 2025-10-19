# https://codeforces.com/problemset/problem/1878/C

for _ in range(int(input())):
    n, k, x = map(int,input().split())
    mn = k*(k+1)//2
    mx = k*(2*n-k+1)//2
    print("YES" if mn<=x<=mx else "NO")
