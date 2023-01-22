def maxConsecutive(bottom: int, top: int, special) -> int:
        special.sort()
        diff =[special[i+1]-special[i]-1 for i in range(len(special)-1)]
        lower=special[0]-bottom
        upper=top-special[-1]
        maxn=0
        if len(diff)>0:
            maxn= max(diff)
        return max(lower,upper,maxn)