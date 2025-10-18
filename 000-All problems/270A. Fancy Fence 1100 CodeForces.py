# https://codeforces.com/problemset/problem/270/A

for _ in range(int(input())):
    a = int(input())
    print("YES" if 360%(180-a) == 0 else "NO")
