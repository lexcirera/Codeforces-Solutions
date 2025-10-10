# https://codeforces.com/problemset/problem/1512/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != a[1] and a[0] != a[2]:
        print(1)
    else:
        for i in range(1, n):
            if a[i] != a[0]:
                print(i + 1)
                break