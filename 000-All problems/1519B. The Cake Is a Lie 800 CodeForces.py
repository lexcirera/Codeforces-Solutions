#https://codeforces.com/problemset/problem/1519/B

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    required_cost = n * m - 1
    if k == required_cost:
        print("YES")
    else:
        print("NO")
