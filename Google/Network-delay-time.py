def networkDelayTime(times, n: int, k: int) -> int:
        matrix = [[float('inf') for _ in range(n)] for _ in range(n)]
        for u,v,w in times:
            matrix[u-1][v-1]=w
        
        dist=[float('inf')]*n
        dist[k-1]=0
        for iter in range(n-1):
            for i in range(n): #u
                for j in range(n): #v
                    if dist[i]!=float('inf') and dist[i]+matrix[i][j]<dist[j]:
                        dist[j]=dist[i]+matrix[i][j]
        if float('inf') in dist:
            return -1
        return max(dist)