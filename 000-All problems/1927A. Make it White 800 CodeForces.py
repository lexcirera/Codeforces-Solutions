# https://codeforces.com/problemset/problem/1927/A

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    l = s.find('B')
    r = s.rfind('B')
    print(r-l+1)
