# https://codeforces.com/problemset/problem/118/A

s = input().lower()
vowels = "aoyeui"
res = ""
for c in s:
    if c not in vowels:
        res += "." + c
print(res)
