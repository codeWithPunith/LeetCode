class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache ={}
        count = Counter(nums)
        nums =sorted(count.keys())
        def helper(i):
            if i in cache:
                return cache[i]
            if i>=len(nums):
                return 0
            include = nums[i]*count[nums[i]]
            if i+1<len(nums) and nums[i]+1==nums[i+1]:
                include = include + helper(i+2)
            else :
                include = include + helper(i+1)
            notInclude = helper(i+1)
            cache[i]=max(include,notInclude)
            return max(include,notInclude)
            
        return helper(0)