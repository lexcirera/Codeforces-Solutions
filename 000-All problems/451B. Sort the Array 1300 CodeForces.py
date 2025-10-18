# https://codeforces.com/problemset/problem/451/B

n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
l, r = -1, -1
for i in range(n):
    if a[i] != b[i]:
        if l == -1:
            l = i
        r = i
if l == -1:
    print("yes\n1 1")
else:
    a[l:r+1] = a[l:r+1][::-1]
    if a == b:
        print("yes")
        print(l+1, r+1)
    else:
        print("no")
