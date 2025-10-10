# https://codeforces.com/problemset/problem/1409/A

for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a - b)
    print((diff + 9) // 10)
