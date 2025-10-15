#https://codeforces.com/problemset/problem/598/A

t = int(input())
for _ in range(t):
    n = int(input())
    total_sum = n * (n + 1) // 2

    power = 1
    power_sum = 0
    while power <= n:
        power_sum += power
        power *= 2

    result = total_sum - 2 * power_sum
    print(result)
