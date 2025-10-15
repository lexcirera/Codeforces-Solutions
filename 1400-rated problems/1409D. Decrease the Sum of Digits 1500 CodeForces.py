#https://codeforces.com/problemset/problem/1409/D

def sum_of_digits(x):
    return sum(int(d) for d in str(x))

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())

    if sum_of_digits(n) <= s:
        print(0)
        continue

    moves = 0
    power = 1
    while True:
        digit = (n // power) % 10
        if digit != 0:
            increment = power * (10 - digit)
            n += increment
            moves += increment
        if sum_of_digits(n) <= s:
            print(moves)
            break
        power *= 10







