# https://codeforces.com/problemset/problem/1692/A

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(sum(x > a for x in [b, c, d]))
