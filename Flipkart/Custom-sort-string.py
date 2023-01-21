from collections import Counter
def customSortString(self, order: str, s: str) -> str:
        d1=Counter(s)
        perm = ""
        for ch in order:
            if ch in d1.keys():
                perm+=ch*d1[ch]
                del d1[ch]
        for i in d1.keys():
            perm+=i*d1[i]
        return perm