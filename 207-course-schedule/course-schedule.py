class Solution:

    def tps(self,node,adj,visited,path):
        if not adj[node]:
            return True
        if node in path:
            return False
        if node in visited:
            return True
        path.add(node)
        for nei in adj[node]:
            if not self.tps(nei,adj,visited,path):
                return False
        path.remove(node)
        visited.add(node)
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i]=[]
        for post,pre in prerequisites:
            adj[pre].append(post)
        visited = set()
        for i in range(numCourses):
            path=set()
            if not self.tps(i,adj,visited,path):
                return False
            visited.add(i)
        return True
        
        