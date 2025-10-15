# https://codeforces.com/problemset/problem/379/A

a, b = map(int, input().split())
hours = a
while a >= b:
    new = a // b
    hours += new
    a = new + a % b
print(hours)

