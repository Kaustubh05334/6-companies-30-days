def numMatchingSubseq(s: str, words) -> int:
        count =0
        for i in words:
            if len(i)>len(s):
                continue
            if i==s:
                count+=1
                continue
            x =0
            for j in s:
                if x==len(i)-1 and i[x]==j:
                    count+=1
                    break
                if i[x]==j:
                    x+=1
        return count