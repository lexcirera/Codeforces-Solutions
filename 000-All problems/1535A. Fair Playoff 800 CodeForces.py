# https://codeforces.com/problemset/problem/1535/A

t = int(input())
for _ in range(t):
    s = list(map(int,input().split()))
    a = max(s[0], s[1])
    b = max(s[2], s[3])
    x = sorted(s)[-2:]
    print("YES" if sorted([a,b])==x else "NO")
