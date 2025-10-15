# https://codeforces.com/problemset/problem/1342/A

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    diff = abs(x - y)
    same = min(x, y)
    print(diff * a + same * min(2 * a, b))
