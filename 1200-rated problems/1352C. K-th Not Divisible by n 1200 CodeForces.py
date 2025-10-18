# https://codeforces.com/problemset/problem/1352/C

for _ in range(int(input())):
    n, k = map(int,input().split())
    print(k + (k-1)//(n-1))
