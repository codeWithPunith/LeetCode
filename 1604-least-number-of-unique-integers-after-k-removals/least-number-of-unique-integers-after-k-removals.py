class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = defaultdict(int)
        for n in arr:
            count[n]+=1
        minheap = []
        for key,val in count.items():
            heapq.heappush(minheap,(val,key))
        
        while k>0:
            if minheap[0][0]<=k:
                val,ele = heapq.heappop(minheap)
                k-=val
                continue
            else:
                break
        return len(minheap)
        