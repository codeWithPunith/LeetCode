class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        nums = sorted(count.keys())
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]*count[nums[0]]
        dp=[0]*len(nums)
        dp[0]=nums[0]*count[nums[0]]
        if nums[0]+1==nums[1]:
            dp[1] = max(nums[1]*count[nums[1]],dp[0])
        else:
            dp[1] = max(nums[1]*count[nums[1]]+dp[0],dp[0])
        for i in range(2,len(nums)):
            include = nums[i]*count[nums[i]]
            if nums[i-1]!=nums[i]-1:
                include = include+dp[i-1]
            else:
                include = include+dp[i-2]
            dp[i]=max(include,dp[i-1])
        return dp[-1]
            

