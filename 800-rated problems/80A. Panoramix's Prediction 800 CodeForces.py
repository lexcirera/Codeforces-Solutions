# https://codeforces.com/problemset/problem/80/A

n, m = map(int,input().split())
def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
p = n+1
while not prime(p):
    p += 1
print("YES" if p == m else "NO")
