# https://codeforces.com/problemset/problem/339/B

n, m = map(int, input().split())
a = list(map(int, input().split()))

pos = 1
time = 0

for task in a:
    if task >= pos:
        time += task - pos
    else:
        time += n - (pos - task)
    pos = task

print(time)
