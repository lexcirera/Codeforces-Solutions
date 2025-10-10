# https://codeforces.com/problemset/problem/1352/A

t = int(input())
for _ in range(t):
    n = input()
    res = []
    for i, d in enumerate(reversed(n)):
        if d != '0':
            res.append(str(int(d) * (10 ** i)))
    print(len(res))
    print(' '.join(res))
