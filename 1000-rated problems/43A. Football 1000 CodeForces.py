# https://codeforces.com/problemset/problem/43/A

n = int(input())
teams = {}
for _ in range(n):
    team = input().strip()
    teams[team] = teams.get(team, 0) + 1
print(max(teams, key=teams.get))