class Solution:
    def ts(self,node,visited,path,res,adj):
            if node==[]:
                return True
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            for nei in adj[node]:
                if not self.ts(nei,visited,path,res,adj):
                    return False
            path.remove(node)
            visited.add(node)
            res.append(node)
            return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj={}
        for i in range(numCourses):
            adj[i]=[]
        for post,pre in prerequisites:
            adj[pre].append(post)
        res=[]
        visited=set()
        
        for i in range(numCourses):
            path=set()
            
            if not self.ts(i,visited,path,res,adj):
                return []
        res.reverse()
        return res
        