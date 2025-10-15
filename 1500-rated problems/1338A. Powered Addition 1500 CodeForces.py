# https://codeforces.com/problemset/problem/1338/A

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mx = arr[0]
    diff = 0
    for v in arr[1:]:
        if v < mx:
            diff = max(diff, mx - v)
        else:
            mx = v
    out.append(str(diff.bit_length()))
print("\n".join(out))


