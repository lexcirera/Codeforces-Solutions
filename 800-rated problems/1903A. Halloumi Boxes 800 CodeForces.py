# https://codeforces.com/problemset/problem/1903/A

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print("YES" if k > 1 or a == sorted(a) else "NO")