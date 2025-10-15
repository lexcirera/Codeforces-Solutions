# https://codeforces.com/problemset/problem/1400/D

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    suffix = [0] * (n + 1)
    for v in a:
        suffix[v] += 1
    ans = 0
    for k in range(n):
        suffix[a[k]] -= 1
        cnt = 0
        ak = a[k]
        for j in range(k):
            ans += cnt * suffix[a[j]]
            if a[j] == ak:
                cnt += 1
    print(ans)