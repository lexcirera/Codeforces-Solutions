# https://codeforces.com/problemset/problem/116/A

n = int(input())
curr = 0
cap = 0
for _ in range(n):
    a, b = map(int, input().split())
    curr = curr - a + b
    cap = max(cap, curr)
print(cap)
