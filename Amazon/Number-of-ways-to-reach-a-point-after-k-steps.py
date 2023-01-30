def numberOfWays(startPos: int, endPos: int, k: int,memo={}) -> int:
        if startPos==endPos and k==0:
            return 1
        if k==0:
            return 0
        if (startPos,k) in memo:
            return memo[(startPos,k)]
        memo[(startPos,k)]=numberOfWays(startPos-1,endPos,k-1,memo)+numberOfWays(startPos+1,endPos,k-1,memo)
        return memo[(startPos,k)]%(10**9+7)


print(numberOfWays(2,5,10))