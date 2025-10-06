# https://codeforces.com/problemset/problem/1030/A

n = int(input())
opinions = list(map(int, input().split()))
print("HARD" if 1 in opinions else "EASY")
