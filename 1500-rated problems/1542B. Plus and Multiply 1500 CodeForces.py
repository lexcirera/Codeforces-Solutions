# https://codeforces.com/problemset/problem/1542/B


t = int(input())
for _ in range(t):
    n, a, b = map(int,input().split())
    ok = False
    if a == 1:
        ok = (n - 1) % b == 0
    else:
        x = 1
        while x <= n:
            if (n - x) % b == 0:
                ok = True
                break
            x *= a
    print("Yes" if ok else "No")





