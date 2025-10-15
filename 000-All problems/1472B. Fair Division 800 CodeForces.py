# https://codeforces.com/problemset/problem/1472/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c1 = a.count(1)
    c2 = a.count(2)
    s = c1+2*c2
    if s%2 != 0:
        print("NO")
    else:
        if s//2%2 == 0 or c1 != 0:
            print("YES")
        else:
            print("NO")
