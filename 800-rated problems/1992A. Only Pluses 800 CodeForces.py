# https://codeforces.com/problemset/problem/1992/A

for _ in range(int(input())):
    a, b, c = sorted(map(int,input().split()))
    for _ in range(5):
        a += 1
        a, b, c = sorted([a,b,c])
    print(a*b*c)
