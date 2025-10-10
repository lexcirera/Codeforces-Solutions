# https://codeforces.com/problemset/problem/1878/A

t=int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if a.count(k) == 0:
        print("NO")
        continue
    ok = False
    for i in range(n-1):
        if a[i] == k or a[i+1] == k:
            ok = True
            break
    if n == 1:
        ok = a[0]==k
    print("YES" if ok else "NO")
