class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        minHeap=[]
        for k,v in freq.items():
            heapq.heappush(minHeap,(v,-k))
        res=[]
        while minHeap:
            occurance,ele = heapq.heappop(minHeap)
            ele=-ele
            while occurance>0:
                res.append(ele)
                occurance-=1
        return res
        

        