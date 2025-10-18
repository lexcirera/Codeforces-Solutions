# https://codeforces.com/problemset/problem/313/A

n = input()
if n[0] != '-':
    print(n)
else:
    a = int(n[:-1])
    b = int(n[:-2]+n[-1])
    print(max(a, b))
