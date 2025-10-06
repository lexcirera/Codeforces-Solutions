# https://codeforces.com/problemset/problem/263/A

for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        r, c = i + 1, row.index(1) + 1
        print(abs(r - 3) + abs(c - 3))
        break
