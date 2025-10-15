#https://codeforces.com/problemset/problem/1858/B

t = int(input())
for _ in range(t):
    n, m, d = map(int, input().split())
    s = list(map(int, input().split()))
    #Sentinels
    a = [1] + s + [n+1]

    # Knapsack-eats per gap
    G = []
    for k in range(len(a)-1):
        diff = a[k+1] - a[k] - 1
        g = diff // d
        if g < 0:
            g = 0
        G.append(g)

    #Total eaten with no removals
    sumG = sum(G)
    eaten0 = m + sumG + (1 if a[1] > 1 else 0)



    best_delta = 10**30
    ways = 0
    # try removing each seller at a[j], j=1..m and keep track
    # in the best delta between no removal and best removal
    for j in range(1, m+1):
        removed_seller = 1 if a[j] != 1 else 0
        leftG  = G[j-1]
        rightG = G[j]
        merged = a[j+1] - a[j-1] - 1
        M = merged // d
        if M < 0:
            M = 0

        delta = M - removed_seller - leftG - rightG
        if delta < best_delta:
            best_delta = delta
            ways = 1
        elif delta == best_delta:
            ways += 1
    print(eaten0 + best_delta, ways)





