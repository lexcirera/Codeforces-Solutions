# https://codeforces.com/problemset/problem/703/A

n = int(input())
m, c = 0, 0
for _ in range(n):
    x, y = map(int,input().split())
    if x > y:
        m += 1
    elif x < y:
        c += 1
print("Mishka" if m > c else "Chris" if c > m else "Friendship is magic!^^")
