# https://codeforces.com/problemset/problem/2044/B

for _ in range(int(input())):
    a = input().strip()
    b = ''
    for c in a[::-1]:
        if c == 'p':
            b += 'q'
        elif c == 'q':
            b += 'p'
        else:
            b += 'w'
    print(b)
