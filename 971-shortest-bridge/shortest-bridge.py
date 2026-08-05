class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #get a certiain island in the q
        d=[[1,0],[0,1],[-1,0],[0,-1]]
        q=deque()
        def inbounds(r,c):
            if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]):
                return True
            return False
        def bfs(r,c):
            level=0
            while q:
                size = len(q)
                for _ in range(size):
                    cr,cc = q.popleft()
                    for dr,dc in d:
                        nr,nc=dr+cr,dc+cc
                        if not inbounds(nr,nc):
                            continue

                        if grid[nr][nc]==2:
                           continue
                        if grid[nr][nc]==1:
                            return level
                        grid[nr][nc]=2
                        q.append((nr,nc))
                level+=1
                    
        def getIslandInQ(r,c,visited):
            if not inbounds(r,c):
                return 
            if grid[r][c]==0 or (r,c) in visited:
                return 
            visited.add((r,c))
            grid[r][c]=2
            q.append((r,c))
            for dr,dc in d:
                getIslandInQ(dr+r,dc+c,visited)
                   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    getIslandInQ(i,j,set())
                    return bfs(i,j)
                    break
        return level
