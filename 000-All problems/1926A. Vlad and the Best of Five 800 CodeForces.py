# https://codeforces.com/problemset/problem/1926/A

t = int(input())
for _ in range(t):
    s = input().strip()
    print("A" if s.count("A")>s.count("B") else "B")
