# https://codeforces.com/problemset/problem/1520/B

for _ in range(int(input())):
    n = int(input())
    l = len(str(n))
    ans = (l-1)*9
    d = int(str(n)[0])
    if int(str(d)*l)<=n:
        ans += d
    else:
        ans += d-1
    print(ans)
