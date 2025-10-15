#https://codeforces.com/problemset/problem/25/A

n = int(input())
nums = list(map(int,input().split()))
even = [i for i,num in enumerate(nums,1) if num%2==0]
odd = [i for i,num in enumerate(nums,1) if num%2==1]
print(even[0] if len(even )== 1 else odd[0])
