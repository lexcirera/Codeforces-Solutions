# https://codeforces.com/problemset/problem/1760/B

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print(max(ord(c)-96 for c in s))
