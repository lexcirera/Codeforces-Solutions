# https://codeforces.com/problemset/problem/1542/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    odd = sum(x%2 for x in a)
    print("Yes" if odd == n else "No")
