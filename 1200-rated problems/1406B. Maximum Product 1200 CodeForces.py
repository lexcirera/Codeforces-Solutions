#https://codeforces.com/problemset/problem/1406/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = []
    c.append(a[-1] * a[-2] * a[-3] * a[-4] * a[-5])
    c.append(a[0] * a[1] * a[2] * a[3] * a[4])
    c.append(a[0] * a[1] * a[2] * a[3] * a[-1])
    c.append(a[0] * a[1] * a[2] * a[-1] * a[-2])
    c.append(a[0] * a[1] * a[-1] * a[-2] * a[-3])
    c.append(a[0] * a[-1] * a[-2] * a[-3] * a[-4])
    print(max(c))