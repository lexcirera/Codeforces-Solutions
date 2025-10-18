# https://codeforces.com/problemset/problem/318/A

n , k = map(int,input().split())
m = (n+1)//2
print(2*k-1 if k<=m else 2*(k-m))
