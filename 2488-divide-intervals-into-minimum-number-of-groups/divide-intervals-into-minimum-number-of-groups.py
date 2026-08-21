class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        minheap=[]
        intervals.sort(key=lambda x:x[0])
        for start,end in intervals:
            if not minheap:
                heapq.heappush(minheap,end)
                continue
            if start <= minheap[0]:
                heapq.heappush(minheap,end)
            else:
                ele = heapq.heappop(minheap)
                ele = end 
                heapq.heappush(minheap,ele)
        return len(minheap)
                    

        