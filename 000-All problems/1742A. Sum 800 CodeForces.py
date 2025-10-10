# https://codeforces.com/problemset/problem/1742/A

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print("YES" if a + b == c or a + c == b or b + c == a else "NO")
