def findIntegers(n):
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1]+f[-2])
        ans, last_seen = 0, 0
        for i in reversed(range(30)):
            if (1 << i) & n:
                ans += f[i]
                if last_seen: 
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans+1