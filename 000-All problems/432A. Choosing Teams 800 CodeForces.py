# https://codeforces.com/problemset/problem/432/A

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = sum(1 for x in a if x + k <= 5)
print(cnt // 3)
