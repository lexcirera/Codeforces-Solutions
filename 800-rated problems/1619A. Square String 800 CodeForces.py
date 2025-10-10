# https://codeforces.com/problemset/problem/1619/A

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if len(s)%2 == 0 and s[:len(s)//2] == s[len(s)//2:] else "NO")
