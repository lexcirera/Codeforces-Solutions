# https://codeforces.com/problemset/problem/1722/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    ok = True
    for i in range(n):
        if (a[i]=='R') != (b[i]=='R'):
            ok = False
            break
    print("YES" if ok else "NO")
