#https://codeforces.com/problemset/problem/1360/D

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    min_packages = n  # worst case: 1-shovel packages

    i = 1
    while i * i <= n:
        if n % i == 0:
            if i <= k:
                min_packages = min(min_packages, n // i)
            if n // i <= k:
                min_packages = min(min_packages, i)
        i += 1
    print(min_packages)