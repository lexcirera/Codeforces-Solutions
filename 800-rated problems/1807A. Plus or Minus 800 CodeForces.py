# https://codeforces.com/problemset/problem/1807/A

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('+' if a + b == c else '-')
