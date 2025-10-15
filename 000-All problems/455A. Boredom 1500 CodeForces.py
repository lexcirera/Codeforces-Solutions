#https://codeforces.com/problemset/problem/455/A

n = int(input())
a = list(map(int, input().split()))
MAX = 10**5 + 2
cnt = [0] * MAX
for x in a:
    cnt[x] += 1

dp = [0] * MAX
dp[0] = 0
dp[1] = cnt[1] * 1

for x in range(2, MAX):
    dp[x] = max(dp[x-1], dp[x-2] + cnt[x] * x)

print(dp[MAX-1])









