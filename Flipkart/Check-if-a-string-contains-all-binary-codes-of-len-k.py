def hasAllCodes(self, s: str, k: int):     
        n=len(s)
        countn=2 ** k        
        visited=set()
        for i in range(n-k+1):
            temp=s[i:i+k]
            if temp not in visited:
                visited.add(temp)
                countn-=1
                if countn==0:
                    return True
        return False