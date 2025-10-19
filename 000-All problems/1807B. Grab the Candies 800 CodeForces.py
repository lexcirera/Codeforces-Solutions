# https://codeforces.com/problemset/problem/1807/B

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    even = sum(x for x in a if x%2==0)
    odd = sum(x for x in a if x%2)
    print("YES" if even>odd else "NO")
