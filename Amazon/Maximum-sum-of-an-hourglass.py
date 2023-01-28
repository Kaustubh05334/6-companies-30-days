def maxSum(grid) -> int:
        row=len(grid)
        col =len(grid[0])
        moves=[(0,1),(0,2),(1,1),(2,0),(2,1),(2,2)]
        ans=0
        for i in range(row-2):
            temp =0
            for j in range(col-2):
                temp+=grid[i][j]
                for x,y in moves:
                    temp+=grid[i+x][j+y]
                if temp>ans:
                    ans=temp
                temp=0  
        return ans