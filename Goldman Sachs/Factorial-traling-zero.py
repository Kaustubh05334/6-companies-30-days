def trailingZeroes(n: int) -> int:
    if n==0:
        return 0
    x = 1
    for i in range(2,n+1):
        x*=i
    x=str(x)
    count=0
    for j in range(len(x)-1,1,-1):
        if x[j]=="0":
            count+=1
        else:
            break
    return count