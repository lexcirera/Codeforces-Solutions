# https://codeforces.com/problemset/problem/1520/A

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ok = True
    seen = set()
    for i in range(n):
        if i>0 and s[i]!=s[i-1] and s[i] in seen:
            ok = False
            break
        seen.add(s[i])
    print("YES" if ok else "NO")
