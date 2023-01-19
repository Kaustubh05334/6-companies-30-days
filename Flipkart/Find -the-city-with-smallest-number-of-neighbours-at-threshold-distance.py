from heapq import heappop,heappush
from collections import defaultdict
def bfs(node: int, adj, maximum: int) -> int:
		heap = []
		heappush(heap,(0,node,-1))
		s = set()

		while heap:

			distance,curr,parent = heappop(heap)

			if distance > maximum:
				continue
			if curr in s:
				continue

			s.add(curr)

			for nextt,price in adj[curr]:
				if nextt != parent:
					heappush(heap,(distance+price,nextt,curr))

		return len(s) - 1



def findTheCity(n: int, edges, distanceThreshold: int) -> int:
		adj = defaultdict(list)
		arr = [0]*n
		for node_1, node_2, price in edges:
			adj[node_1].append((node_2,price))
			adj[node_2].append((node_1,price))
		for i in range(n):
			done = bfs(i,adj,distanceThreshold)
			arr[i] = done

		min_node = min(arr)
		ans = 0
		for i in range(len(arr)):
			if arr[i] == min_node:
				ans = i
		return ans