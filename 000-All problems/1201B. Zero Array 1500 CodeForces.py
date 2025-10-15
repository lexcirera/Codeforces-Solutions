# https://codeforces.com/problemset/problem/1201/B

n = int(input())
arr = list(map(int, input().split()))
total, mx = sum(arr), max(arr)
if total % 2 == 0 and mx <= total - mx:
    print("YES")
else:
    print("NO")






