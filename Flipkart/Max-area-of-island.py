from collections import deque
def maxAreaOfIsland(grid) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        curArea = 0
        maxArea = 0
    
        def bfs(r,c):
            queue = deque()
            area = 1
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                row, col = queue.popleft()
                directions = [
                    [1,0], 
                    [-1,0],   
                    [0,1], 
                    [0,-1]
                ]
                for dr, dc in directions:
                    r,c = row+dr,col+dc
                    if (
                        r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == 1 and
                        (r,c) not in visited
                    ):
                        visited.add((r,c))
                        queue.append((r,c))
                        area += 1
            return area                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    curArea = bfs(r,c)
                    maxArea = max(maxArea, curArea)

        return maxArea