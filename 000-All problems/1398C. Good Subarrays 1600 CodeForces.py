# https://codeforces.com/problemset/problem/1398/C

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    freq = {0:1}
    curr = 0
    ans = 0
    for ch in s:
        curr += ord(ch)-49 #ord('1') = 49
        ans += freq.get(curr,0)
        freq[curr] = freq.get(curr,0) + 1
    print(str(ans))