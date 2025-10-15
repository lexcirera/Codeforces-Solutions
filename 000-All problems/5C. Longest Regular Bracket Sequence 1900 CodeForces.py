#https://codeforces.com/problemset/problem/5/C

s = input().strip()
stack = [-1]
longest, cnt = 0, 0

for i, char in enumerate(s):
    if char == '(':
        stack.append(i)
    else:
        stack.pop()
        if stack:
            length = i - stack[-1]
            if length > longest:
                longest = length
                cnt = 1
            elif length == longest:
                cnt += 1
        else:
            stack.append(i)
if longest == 0:
    print(0,1)
else:
    print(longest, cnt)