# https://codeforces.com/problemset/problem/758/A

n = int(input())
a = list(map(int, input().split()))
print(sum(max(a) - x for x in a))
