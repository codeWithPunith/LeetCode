class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #lets do this with dfs
        d=[[1,0],[0,1],[-1,0],[0,-1]]

        def inbounds(r,c):
            if r>=0 and c>=0 and r<len(image) and c<len(image[0]):
                return True
            return False
        def dfs(r,c,prevColor):
            if not inbounds(r,c):
                return 
            for dr,dc in d:
                nr,nc=r+dr,c+dc
                if inbounds(nr,nc) and image[nr][nc]==prevColor and image[nr][nc]!=color:
                    image[nr][nc]=color
                    dfs(nr,nc,prevColor)
        ogcolor = image[sr][sc]          
        image[sr][sc]=color
        dfs(sr,sc,ogcolor)

        return image
                





        