# https://codeforces.com/problemset/problem/785/A

n = int(input())
d = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
res = 0
for _ in range(n):
    res += d[input()]
print(res)
