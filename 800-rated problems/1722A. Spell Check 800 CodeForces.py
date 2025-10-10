# https://codeforces.com/problemset/problem/1722/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print("YES" if n == 5 and sorted(s) == sorted("Timur") else "NO")
