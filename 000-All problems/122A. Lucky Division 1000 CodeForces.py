# https://codeforces.com/problemset/problem/122/A

n = int(input())
nums = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

print("YES" if any(n % x == 0 for x in nums) else "NO")
