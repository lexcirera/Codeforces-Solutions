# https://codeforces.com/problemset/problem/268/A

n = int(input())
teams = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if i != j and teams[i][0] == teams[j][1]:
            ans += 1
print(ans)
