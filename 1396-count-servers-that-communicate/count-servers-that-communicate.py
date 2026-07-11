class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowServer =[0]*m
        colServer = [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rowServer[i]+=1
                    colServer[j]+=1
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rowServer[i]>1 or colServer[j]>1):
                    res+=1

        return res