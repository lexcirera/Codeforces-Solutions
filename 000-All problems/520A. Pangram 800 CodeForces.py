# https://codeforces.com/problemset/problem/520/A

n = int(input())
s = input().lower()
print("YES" if len(set(s)) == 26 else "NO")
