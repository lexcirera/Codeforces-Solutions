# https://codeforces.com/problemset/problem/1955/A

for _ in range(int(input())):
    n, a, b = map(int,input().split())
    print((n//2)*min(2*a,b)+(n%2)*a)
