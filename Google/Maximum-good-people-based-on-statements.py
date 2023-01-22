def maximumGood(arr) -> int:
        n, ans = len(arr), 0
    
        def check(perm):
            for i in range(n):
                if perm[i] == '0': continue
                for j in range(n):
                    if arr[i][j] == 2: continue
                    if (arr[i][j] == 1 and perm[j] == '0') or (arr[i][j] == 0 and perm[j] == '1'): 
                        return False
            return True

        for num in range(1 << n, 1 << (n + 1)):
            permutation = bin(num)[3:]
            if check(permutation): 
                ans = max(ans, permutation.count('1'))
        return ans