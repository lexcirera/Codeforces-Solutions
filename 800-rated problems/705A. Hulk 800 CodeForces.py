# https://codeforces.com/problemset/problem/705/A

n = int(input())
res = []
for i in range(1, n + 1):
    res.append("I hate" if i % 2 else "I love")
print(" that ".join(res) + " it")
