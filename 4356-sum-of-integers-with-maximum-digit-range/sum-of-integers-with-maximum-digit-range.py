class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        res=[]
        for i,n in enumerate(nums):
            small = float("inf")
            large = float("-inf")
            while n :
                digit = n%10
                small = min(small,digit)
                large = max(large,digit)
                n=n//10
            res.append(((large-small)*-1,nums[i]))

        minheap=res.copy()
        heapq.heapify(minheap)
        Range,number = heapq.heappop(minheap)
        Range = -Range
        while minheap and minheap[0][0]== -Range:
            _,heapele=heapq.heappop(minheap)
           
            number+=heapele
        return number
        