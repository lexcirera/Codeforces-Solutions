# https://codeforces.com/problemset/problem/189/A

n, a, b, c = map(int,input().split())
dp = [float("-inf")]*(n+1)
dp[0] = 0
for i in range(1,n+1):
    for x in (a, b, c):
        if i >= x:
            dp[i] = max(dp[i], dp[i-x]+1)
print(dp[n])
