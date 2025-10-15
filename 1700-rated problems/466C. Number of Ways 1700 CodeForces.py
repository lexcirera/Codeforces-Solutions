# https://codeforces.com/problemset/problem/466/C

def solve(n, a):
    if n<3:
        print(0)
        return

    s = sum(a)
    if s%3 != 0:
        print(0)
        return

    t, prefix, cnt, ans = s//3, 0, 0, 0
    for i in range(n-1):
        prefix += a[i]
        if prefix == 2*t:
            ans += cnt
        if prefix == t:
            cnt += 1
    print(ans)
    return


n = int(input())
a = list(map(int, input().split()))
solve(n,a)



