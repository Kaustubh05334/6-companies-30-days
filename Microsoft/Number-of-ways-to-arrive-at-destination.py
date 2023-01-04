from collections import defaultdict
from heapq import *
def countPaths(n: int, roads) -> int:
    graph = defaultdict(list)
    for u, v, time in roads:
        graph[u].append([v, time])
        graph[v].append([u, time])

    def dijkstra(src):
        dist = [float("inf")] * n
        ways = [0] * n
        minHeap = [(0, src)]  # dist, src
        dist[src] = 0
        ways[src] = 1
        while minHeap:
            d, u = heappop(minHeap)
            if dist[u] < d: continue  
            for v, time in graph[u]:
                if dist[v] > d + time:
                    dist[v] = d + time
                    ways[v] = ways[u]
                    heappush(minHeap, (dist[v], v))
                elif dist[v] == d + time:
                    ways[v] = (ways[v] + ways[u]) % (10**9+7)
        return ways[n - 1]

    return dijkstra(0)