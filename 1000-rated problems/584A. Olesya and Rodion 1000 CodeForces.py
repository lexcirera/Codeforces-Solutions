# https://codeforces.com/problemset/problem/584/A

n, t = map(int, input().split())
if n == 1 and t == 10:
    print(-1)
else:
    print(str(t) + '0' * (n - len(str(t))))
