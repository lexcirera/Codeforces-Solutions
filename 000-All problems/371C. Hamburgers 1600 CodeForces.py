# https://codeforces.com/problemset/problem/371/C

s = input().strip()
nb, ns, nc = map(int, input().split())
pb, ps, pc = map(int, input().split()) #prices
r = int(input())

# Ingredients per burger
cntB = s.count('B')
cntS = s.count('S')
cntC = s.count('C')

def canMake(x):
    needB = max(0, cntB * x - nb)
    needS = max(0, cntS * x - ns)
    needC = max(0, cntC * x - nc)
    return needB*pb + needS*ps + needC*pc <= r # cost<= r

# Binary search for maximum cnt
low, high = 0, 10**30
cnt = 0
while low <= high:
    mid = (low + high) // 2
    if canMake(mid):
        cnt = mid
        low = mid + 1
    else:
        high = mid - 1

print(cnt)