import numpy as np
from itertools import zip_longest,islice
from math import log2,floor
def numberOfCombinations(s):
    def ranks(l):
        index = {v: i for i, v in enumerate(sorted(set(l)))}
        return [index[v] for v in l]

    def suffixArray(s):
        line = ranks(s)
        n, k, ans, sa = len(s), 1, [line], [0]*len(s)
        while k < n - 1:
            line = ranks(list(zip_longest(line, islice(line, k, None), fillvalue=-1)))
            ans, k = ans + [line], k << 1
        for i, k in enumerate(ans[-1]): sa[k] = i
        return ans, sa

    def compare(i, j, l, k):
        a = (c[k][i], c[k][(i+l-(1<<k))%n])
        b = (c[k][j], c[k][(j+l-(1<<k))%n])
        return 0 if a == b else 1 if a < b else -1

    c, sa = suffixArray([int(i) for i in s])

    n, M = len(s), 10**9 + 7
    dp = np.zeros([n+1, n+1], dtype = int)
    mp = np.zeros([n+1, n+1], dtype = int)

    for k in range(n+1):
        dp[0][k] = 1
        mp[0][k] = 1

    logs = [0] + [floor(log2(k)) for k in range(1, n+1)]

    s_zero = np.array([i != "0" for i in s], dtype = int)

    for i in range(1, n+1):
        dp[i][1:i+1] = mp[range(i-1,-1,-1), range(i)] * s_zero[i-1::-1]

        check1 = dp[range(i-1, (i-1)//2, -1), range(1, i//2 + 1)]
        f = lambda k: compare(i-2*k, i-k, k, logs[k]) >= 0
        check2 = np.array([f(i) for i in range(1, i//2+1)])

        dp[i][1:i//2+1] = dp[i][1:i//2+1] + check1*check2
        dp[i][1:i//2+1] = [x % M for x in dp[i][1:i//2+1]]

        mp[i] = np.cumsum(dp[i])

    return mp[-1][-1] % M