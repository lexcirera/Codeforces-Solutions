# https://codeforces.com/problemset/problem/514/A

s = list(input())
for i in range(len(s)):
    d = int(s[i])
    if i == 0 and d == 9:
        continue
    if d > 4:
        s[i] = str(9-d)
print(''.join(s))
