# https://codeforces.com/problemset/problem/750/A

n, k = map(int, input().split())
time = 240 - k
total = 0
for i in range(1, n + 1):
    if total + 5 * i > time:
        print(i - 1)
        break
    total += 5 * i
else:
    print(n)
