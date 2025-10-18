# https://codeforces.com/problemset/problem/1343/A

for _ in range(int(input())):
    n = int(input())
    k = 2
    while True:
        d = (1<<k)-1
        if n%d == 0:
            print(n//d)
            break
        k += 1
