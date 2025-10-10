# https://codeforces.com/problemset/problem/490/A

n = int(input())
a = list(map(int, input().split()))
p, m, s = [], [], []
for i in range(n):
    if a[i] == 1:
        p.append(i + 1)
    elif a[i] == 2:
        m.append(i + 1)
    else:
        s.append(i + 1)
w = min(len(p), len(m), len(s))
print(w)
for i in range(w):
    print(p[i], m[i], s[i])
