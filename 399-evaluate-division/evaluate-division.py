class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)
        for i,eq in enumerate(equations):
            a,b=eq
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
        def dfs(src,target,visited):
            if src==target:
                return 1
            visited.add(src)
            for nei,value in adj[src]:
                if nei not in visited:
                    ans = dfs(nei, target, visited)
                    if ans != -1:
                        return value * ans
            return -1
        res=[]
        for num,den in queries:
            if num not in adj or den not in adj:
                res.append(-1.0)
            else:
                res.append(dfs(num, den, set()))
        return res

            

        
            
        
        