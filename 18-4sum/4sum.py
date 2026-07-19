class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i-1]==nums[i]:
                continue

            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                l=j+1
                r=len(nums)-1
                newTarget = target-nums[i]-nums[j]
                while l<r:
                    if nums[l]+nums[r]==newTarget:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l-1]==nums[l]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                        
                    elif nums[l]+nums[r]>newTarget:
                        r-=1
                    else:
                        l+=1
        return res