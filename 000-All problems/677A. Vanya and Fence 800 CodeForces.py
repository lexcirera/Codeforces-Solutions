# https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())
a = list(map(int, input().split()))
print(sum(2 if x > h else 1 for x in a))
