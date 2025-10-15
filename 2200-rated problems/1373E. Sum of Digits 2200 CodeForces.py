#https://codeforces.com/problemset/problem/1373/E



def build_table_for_k(k):
    N = 150
    ans = [None] * (N+1)

    # Initialize p=1
    DP = {}
    for d0 in range(10):
        mask1 = 0
        sum1  = 0
        for i in range(k+1):
            v = d0 + i
            sum1 += v % 10
            if v >= 10:
                mask1 |= (1 << i)
        if sum1 <= N:
            st = chr(ord('0') + d0)
            key = (mask1, sum1)
            if key not in DP or st[::-1] < DP[key][::-1]:
                DP[key] = st

    #populate any ans[sum] that we already reached with mask=0
    for (mask, s), suffix in DP.items():
        if mask == 0 and ans[s] is None:
            ans[s] = suffix[::-1]

    # Now extend to longer prefixes
    max_digits = 20
    for p in range(1, max_digits):
        nextDP = {}
        for (mask, s), suffix in DP.items():
            # again pick off any new answers at this layer
            if mask == 0 and ans[s] is None:
                ans[s] = suffix[::-1]

            for d in range(10):
                new_mask = mask if d == 9 else 0
                pop = mask.bit_count()
                contr = (k+1)*d + pop - (10 * pop if d == 9 else 0)
                ns = s + contr
                if ns > N:
                    continue
                st2 = suffix + chr(ord('0')+d)
                key2 = (new_mask, ns)
                if key2 not in nextDP or st2[::-1] < nextDP[key2][::-1]:
                    nextDP[key2] = st2
        DP = nextDP

    return ans


# Precompute once for all k = 0..9
tables = [build_table_for_k(k) for k in range(10)]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    res = tables[k][n]
    print(int(res) if res is not None else -1)

