# https://codeforces.com/problemset/problem/155/A

n = int(input())
a = list(map(int, input().split()))
best, worst = a[0], a[0]
cnt = 0
for x in a[1:]:
    if x > best or x < worst:
        cnt += 1
    best = max(best, x)
    worst = min(worst, x)
print(cnt)
