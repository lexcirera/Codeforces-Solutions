# https://codeforces.com/problemset/problem/9/A

import math
y, w = map(int, input().split())
fav = 7 - max(y, w)
g = math.gcd(fav, 6)
print(f"{fav // g}/{6 // g}")