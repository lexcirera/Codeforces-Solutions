# https://codeforces.com/problemset/problem/110/A

n = input()
cnt = sum(1 for d in n if d in '47')
print("YES" if str(cnt) in {"4", "7", "44", "47", "74", "77"} else "NO")
