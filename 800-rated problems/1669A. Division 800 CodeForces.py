# https://codeforces.com/problemset/problem/1669/A

for _ in range(int(input())):
    r = int(input())
    if r >= 1900:
        print("Division 1")
    elif r >= 1600:
        print("Division 2")
    elif r >= 1400:
        print("Division 3")
    else:
        print("Division 4")
