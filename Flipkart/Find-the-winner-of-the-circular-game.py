def findTheWinner(n: int, k: int) -> int:
    l1 = [i for i in range(n)]
    idx=0
    while(len(l1)>1):
        idx = (idx+k-1)%n
        l1.pop(idx)
        n-=1
    return l1.pop()+1