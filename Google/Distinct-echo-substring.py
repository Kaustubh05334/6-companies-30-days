def distinctEchoSubstrings(text: str) -> int:
        visited=[]
        for i in range(len(text)):
            for j in range(i,len(text)):
                mid = (j+i)//2
                if text[i:mid+1]==text[mid+1:j+1]:
                    if text[i:mid+1] not in visited:
                        visited.append(text[i:mid+1])
        return len(visited)