# https://codeforces.com/problemset/problem/1858/A

t = int(input())
for _ in range(t):
    a, b, c = map(int,input().split())
    if (a+ (c+1)//2) > (b + c//2):
        print("First")
    else:
        print("Second")
