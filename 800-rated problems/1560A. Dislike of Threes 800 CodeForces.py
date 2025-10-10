# https://codeforces.com/problemset/problem/1560/A

for _ in range(int(input())):
    k = int(input())
    x = 0
    while k:
        x += 1
        if x % 3 != 0 and x % 10 != 3:
            k -= 1
    print(x)
