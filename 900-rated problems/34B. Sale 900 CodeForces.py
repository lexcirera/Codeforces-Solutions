# https://codeforces.com/problemset/problem/34/B

n, m = map(int,input().split())
a = sorted(map(int,input().split()))
ans = 0
for x in a:
    if m == 0 or x >= 0:
        break
    ans += -x
    m -= 1
print(ans)
