# https://codeforces.com/problemset/problem/1857/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if sum(a) % 2 == 0 else "NO")