#https://codeforces.com/problemset/problem/489/C

m,s=map(int,input().split())

if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
elif s > 9*m:
    print("-1 -1")
else:
    remain = s
    maxi = ""
    for _ in range(m):
        digit = min(9,remain)
        maxi+=str(digit)
        remain-=digit
    remain = s-1
    digits=[0]*m
    for i in range(m-1,0,-1):
        digit = min(9,remain)
        digits[i] = digit
        remain -= digit
    digits[0] = remain+1
    mini = "".join(str(digit) for digit in digits)
    print(mini, maxi)