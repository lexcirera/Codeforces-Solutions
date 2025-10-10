# https://codeforces.com/problemset/problem/381/A

n = int(input())
a = list(map(int, input().split()))
l, r = 0, n - 1
s, d, t = 0, 0, 0
while l <= r:
    if a[l] > a[r]:
        x = a[l]
        l += 1
    else:
        x = a[r]
        r -= 1
    if t % 2 == 0:
        s += x
    else:
        d += x
    t += 1
print(s, d)
