def islandDfs(rx, cx, grid, m, n):       
        if rx < 0 or cx < 0 or rx >= m or cx >=n:
            return False
        
        if grid[rx][cx] == 1:
            return True
        if grid[rx][cx] == -1:
            return True
        grid[rx][cx] = -1
        result = True
        for rx, cx in [(rx-1, cx), (rx+1, cx), (rx, cx-1), (rx, cx+1)]:
            if not islandDfs(rx, cx, grid, m, n):
                result = False
        
        return result
def closedIsland(grid) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        for rx in range(m):
            for cx in range(n):
                if grid[rx][cx] == 0 and islandDfs(rx, cx, grid, m, n):
                    result += 1
        return result
    

