# https://codeforces.com/problemset/problem/61/A

a = input()
b = input()
print(''.join('1' if x != y else '0' for x, y in zip(a, b)))
