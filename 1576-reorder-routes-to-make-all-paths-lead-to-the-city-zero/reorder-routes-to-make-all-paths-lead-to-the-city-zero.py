class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        #my intitution is go trogh all nodes starting from zero if any node has a incomming edge just increase the path to be more precise if it has a neighbor who is not taking u to zero 
        adj={}
        res=0
        realEdges = {(a,b) for a,b in connections}
        for i in range(n):
            adj[i]=[]
        for start,end in connections:
            adj[start].append(end)
            adj[end].append(start)
        leadingToZero = set()
        leadingToZero.add(0)
        q = deque()
        q.append(0)
        while q:
            size = len(q)
            for _ in range(size):
                ele = q.popleft()
           
                for nei in adj[ele]:
                    if nei not in leadingToZero:
                        leadingToZero.add(nei)
                        q.append(nei)
                        if (ele,nei) in realEdges:
                            res+=1
                       
                


        return res
        