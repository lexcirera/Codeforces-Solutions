# https://codeforces.com/problemset/problem/474/A

d = input().strip()
s = input().strip()
k = "qwertyuiopasdfghjkl;zxcvbnm,./"
t = []
for c in s:
    i = k.index(c)
    t.append(k[i-1] if d == "R" else k[i+1])
print("".join(t))
