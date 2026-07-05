class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #use of boolean lookup 
        watched =[False]*(len(nums)+1)
        for n in nums:
            if 0<=n<=len(nums):
                watched[n]=True
        for i in range(1,len(nums)+1):
            if not watched[i]:
                return i
        return len(nums)+1
        