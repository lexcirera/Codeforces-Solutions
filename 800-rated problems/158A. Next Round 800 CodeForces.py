# https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())
scores = list(map(int, input().split()))
threshold = scores[k - 1]
count = sum(1 for s in scores if s >= threshold and s > 0)
print(count)
