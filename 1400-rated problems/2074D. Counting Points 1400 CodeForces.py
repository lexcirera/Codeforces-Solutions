#https://codeforces.com/problemset/problem/2074/D

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x_coords = list(map(int, input().split()))
    r_vals = list(map(int, input().split()))

    y_map = dict()

    for i in range(n):
        cx, r = x_coords[i], r_vals[i]
        for y in range(-r, r + 1):
            dx_sq = r * r - y * y
            if dx_sq < 0:
                continue
            dx = int(dx_sq ** 0.5)
            x_start = cx - dx
            x_end = cx + dx
            if y not in y_map:
                y_map[y] = []
            y_map[y].append((x_start, x_end))

    result = 0
    for y in y_map:
        intervals = sorted(y_map[y])
        merged = []
        for x_start, x_end in intervals:
            if not merged or merged[-1][1] < x_start - 1:
                merged.append([x_start, x_end])
            else:
                merged[-1][1] = max(merged[-1][1], x_end)
        for x_start, x_end in merged:
            result += x_end - x_start + 1

    print(result)
