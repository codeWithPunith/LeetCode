class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        res=0
        for i in range(n-2):
            if nums[i]==0:
                nums[i]=1
                nums[i+1]= not nums[i+1]
                nums[i+2]=not nums[i+2]
                res+=1
        if sum(nums)==n:
            return res
        return -1
        