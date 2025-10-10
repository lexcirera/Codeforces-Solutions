# https://codeforces.com/problemset/problem/1760/A

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(sorted([a, b, c])[1])
