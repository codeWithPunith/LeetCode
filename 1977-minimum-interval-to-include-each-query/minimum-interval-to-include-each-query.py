class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minheap =[]
        res,i={},0
        intervals.sort(key = lambda x:x[0])
        for q in sorted(queries):
            while i<len(intervals) and intervals[i][0]<=q:
                l,r=intervals[i]
                heapq.heappush(minheap,(r-l+1,r))
                i+=1
            while minheap and minheap[0][1]<q:
                heapq.heappop(minheap)
            res[q]=minheap[0][0] if minheap else -1
        mapit=[0]*len(queries)
        for i,n in enumerate(queries):
            mapit[i]=res.get(n)
        return mapit
            