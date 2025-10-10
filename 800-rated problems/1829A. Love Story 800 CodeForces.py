# https://codeforces.com/problemset/problem/1829/A

t = int(input())
ref = "codeforces"
for _ in range(t):
    s = input()
    print(sum(s[i] != ref[i] for i in range(10)))