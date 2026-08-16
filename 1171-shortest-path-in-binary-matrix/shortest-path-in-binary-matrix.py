class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        res =-1
        visited =[[False]*len(grid[0]) for _ in range(len(grid))]
        d=[[1,0],[0,1],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        def inBounds(r,c):
            if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]):
                return True
            return False
        
        def bfs():
            nonlocal res
            q = deque()
            q.append((0,0))
            visited[0][0]=True
            shortestPath =1
            while q :
                for _ in range(len(q)):
                    r,c = q.popleft()
                    if r==len(grid)-1 and c==len(grid)-1:
                        res = shortestPath
                        return 
                    for dr,dc in d:
                        nr,nc = r+dr,c+dc
                        if inBounds(nr,nc) and grid[nr][nc] == 0 and not visited[nr][nc]:
                            q.append((nr,nc))
                            visited[nr][nc]=True
                            
                shortestPath+=1
        if grid[0][0]==1:
            return -1
        bfs()
        return res

                    

        