# https://codeforces.com/problemset/problem/1986/A

for _ in range(int(input())):
    x = list(map(int, input().split()))
    x.sort()
    print(x[2]-x[0])
