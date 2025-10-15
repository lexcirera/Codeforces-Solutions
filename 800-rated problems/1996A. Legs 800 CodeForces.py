# https://codeforces.com/problemset/problem/1996/A

t = int(input())
for _ in range(t):
    n = int(input())
    print(n//4 + (n%4)//2)
