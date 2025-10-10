# https://codeforces.com/problemset/problem/1850/A

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("YES" if a + b >= 10 or a + c >= 10 or b + c >= 10 else "NO")
