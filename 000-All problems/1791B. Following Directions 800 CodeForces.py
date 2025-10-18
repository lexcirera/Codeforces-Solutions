# https://codeforces.com/problemset/problem/1791/B

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    x, y = 0, 0
    ok = False
    for c in s:
        if c=='L':
            x -= 1
        elif c=='R':
            x += 1
        elif c=='U':
            y += 1
        else:
            y -= 1
        if x==1 and y==1:
            ok = True
            break
    print("YES" if ok else "NO")
