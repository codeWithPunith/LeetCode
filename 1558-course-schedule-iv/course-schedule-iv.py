class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}

        for pre, post in prerequisites:
            adj[pre].append(post)
        def dfs(src,target,visited):
            
            if src==target:
                return True
            visited.add(src)
            for nei in adj[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False
        
        ans=[]
        for pre,post in queries:
            ans.append(dfs(pre,post,set()))
        return ans
        