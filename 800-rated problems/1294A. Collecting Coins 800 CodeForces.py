# https://codeforces.com/problemset/problem/1294/A

t = int(input())
for _ in range(t):
    a, b, c, n = map(int,input().split())
    m = max(a,b,c)
    d = (m-a)+(m-b)+(m-c)
    print("YES" if n>=d and (n-d)%3==0 else "NO")
