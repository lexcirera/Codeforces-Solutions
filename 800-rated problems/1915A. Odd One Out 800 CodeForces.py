# https://codeforces.com/problemset/problem/1915/A

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a if b == c else b if a == c else c)
