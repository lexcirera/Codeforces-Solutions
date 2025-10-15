# https://codeforces.com/problemset/problem/1669/B

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    ans = -1
    for x in a:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == 3:
            ans = x
            break
    print(ans)
