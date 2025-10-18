# https://codeforces.com/problemset/problem/1475/B

for _ in range(int(input())):
    n = int(input())
    print("YES" if n%2020 <= n//2020 else "NO")
