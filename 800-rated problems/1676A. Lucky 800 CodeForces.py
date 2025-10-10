# https://codeforces.com/problemset/problem/1676/A

for _ in range(int(input())):
    s = input()
    print("YES" if sum(map(int, s[:3])) == sum(map(int, s[3:])) else "NO")
