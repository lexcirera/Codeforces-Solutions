# https://codeforces.com/problemset/problem/2/A

n = int(input())
rounds = []
scores = {}
for _ in range(n):
    name, s = input().split()
    s = int(s)
    rounds.append((name, s))
    scores[name] = scores.get(name, 0) + s
m = max(scores.values())
candidates = {name for name, v in scores.items() if v == m}
current = {}
for name, s in rounds:
    current[name] = current.get(name, 0) + s
    if name in candidates and current[name] >= m:
        print(name)
        break