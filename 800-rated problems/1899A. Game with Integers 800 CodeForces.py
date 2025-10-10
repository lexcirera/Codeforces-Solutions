# https://codeforces.com/problemset/problem/1899/A

for _ in range(int(input())):
    n = int(input())
    print("First" if n % 3 != 0 else "Second")
