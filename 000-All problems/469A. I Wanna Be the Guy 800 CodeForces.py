# https://codeforces.com/problemset/problem/469/A

n = int(input())
x = set(map(int, input().split()[1:]))
y = set(map(int, input().split()[1:]))
print("I become the guy." if len(x | y) == n else "Oh, my keyboard!")
