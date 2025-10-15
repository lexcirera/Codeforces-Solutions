# https://codeforces.com/problemset/problem/550/C

n = input().strip()

# Check all subsets of up to 3 digits (since any number divisible by 8 is determined by its last 3 digits)
found = False
length = len(n)

# First check single digits
for i in range(length):
    num = int(n[i])
    if num % 8 == 0:
        print("YES")
        print(num)
        found = True
        break

# Check two-digit combinations
if not found:
    for i in range(length):
        for j in range(i + 1, length):
            num = int(n[i] + n[j])
            if num % 8 == 0:
                print("YES")
                print(num)
                found = True
                break
        if found:
            break

# Check three-digit combinations
if not found:
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                num = int(n[i] + n[j] + n[k])
                if num % 8 == 0:
                    print("YES")
                    print(num)
                    found = True
                    break
            if found:
                break
        if found:
            break

if not found:
    print("NO")
