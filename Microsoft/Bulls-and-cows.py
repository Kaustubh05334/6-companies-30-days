from collections import Counter
def getHint(self, secret: str, guess: str) -> str:
    numbulls=0
    numcows=0
    ser = Counter(secret)
    gue = Counter(guess)
    for i in range(len(secret)):
        if secret[i]==guess[i]:
            numbulls+=1
            ser[secret[i]]-=1
            gue[secret[i]]-=1
    for i in ser.keys():
        if i in gue:
            numcows+=min(ser[i],gue[i])
    
    return f"{numbulls}A{numcows}B"