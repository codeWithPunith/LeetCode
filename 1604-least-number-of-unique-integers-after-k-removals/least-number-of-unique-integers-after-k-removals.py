class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)

        
        minheap = [(key,val) for val ,key in count.items()]
        # for key,val in count.items():
        #     heapq.heappush(minheap,(val,key))
        heapq.heapify(minheap)
        while k>0:
            if minheap[0][0]<=k:
                val,ele = heapq.heappop(minheap)
                k-=val
                continue
            else:
                break
        return len(minheap)
        