# https://codeforces.com/problemset/problem/1900/A

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    if '...' in s:
        print(2)
    else:
        print(s.count('.'))
