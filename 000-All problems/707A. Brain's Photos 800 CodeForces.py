# https://codeforces.com/problemset/problem/707/A

n, m = map(int,input().split())
c = set()
for _ in range(n):
    c |= set(input().split())
print("#Color" if any(x in c for x in "CMY") else "#Black&White")
