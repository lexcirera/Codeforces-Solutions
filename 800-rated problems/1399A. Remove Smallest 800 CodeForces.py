# https://codeforces.com/problemset/problem/1399/A

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    print("YES" if all(a[i+1]-a[i]<=1 for i in range(n-1)) else "NO")
