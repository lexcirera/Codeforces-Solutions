# https://codeforces.com/problemset/problem/451/A

n, m = map(int, input().split())
print("Akshat" if min(n, m)%2 else "Malvika")
