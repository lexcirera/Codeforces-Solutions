# https://codeforces.com/problemset/problem/1526/C1

import heapq

n = int(input())
potions = list(map(int, input().split()))
health = 0
potionsQueue = []
for potion in potions:
    if health + potion >= 0:
        health += potion
        heapq.heappush(potionsQueue, potion)
    elif potionsQueue and potionsQueue[0] < potion:
        health += potion - heapq.heapreplace(potionsQueue, potion)
print(len(potionsQueue))
