# https://codeforces.com/problemset/problem/1881/A

for _ in range(int(input())):
    n, m = map(int,input().split())
    x = input().strip()
    s = input().strip()
    ans = -1
    for i in range(6):
        if s in x:
            ans = i
            break
        x += x
    print(ans)
