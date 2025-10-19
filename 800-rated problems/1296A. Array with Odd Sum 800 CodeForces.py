# https://codeforces.com/problemset/problem/1296/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    if s%2==1 or (any(x%2 for x in a) and any(x%2==0 for x in a)):
        print("YES")
    else:
        print("NO")
