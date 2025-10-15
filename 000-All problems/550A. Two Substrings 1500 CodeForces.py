# https://codeforces.com/problemset/problem/550/A

s = input().strip()
idx1, idx2 = s.find("AB"), s.find("BA")
if (idx1!=-1 and s.find("BA",idx1+2)!=-1) or (idx2!=-1 and s.find("AB",idx2+2)!=-1):
    print("YES")
else:
    print("NO")


