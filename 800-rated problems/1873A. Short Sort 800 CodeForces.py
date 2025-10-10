# https://codeforces.com/problemset/problem/1873/A

for _ in range(int(input())):
    s = input()
    print("YES" if s in ["abc", "acb", "bac", "cba"] else "NO")
