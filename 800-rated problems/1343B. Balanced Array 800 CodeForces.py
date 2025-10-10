# https://codeforces.com/problemset/problem/1343/B

t = int(input())
for _ in range(t):
    n = int(input())
    if (n//2)%2:
        print("NO")
    else:
        print("YES")
        a = [2*i for i in range(1, n//2+1)]
        b = [2*i-1 for i in range(1, n//2)]
        b.append(a[-1]+n//2-1)
        print(*(a+b))
