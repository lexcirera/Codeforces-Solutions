# https://codeforces.com/problemset/problem/1807/D

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    total = prefix[n]
    for _ in range(q):
        l, r, k = map(int, input().split())
        seg = prefix[r] - prefix[l - 1]
        new = total - seg + (r - l + 1) * k
        print("YES" if new % 2 else "NO")
