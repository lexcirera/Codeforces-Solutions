# https://codeforces.com/problemset/problem/1915/B

for _ in range(int(input())):
    r = [input().strip() for _ in range(3)]
    for row in r:
        if '?' in row:
            s = set(row.replace('?',''))
            for c in 'ABC':
                if c not in s:
                    print(c)
                    break
            break