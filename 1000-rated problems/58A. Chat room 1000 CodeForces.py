# https://codeforces.com/problemset/problem/58/A

s = input()
target = "hello"
j = 0
for c in s:
    if c == target[j]:
        j += 1
        if j == len(target):
            break
print("YES" if j == len(target) else "NO")
