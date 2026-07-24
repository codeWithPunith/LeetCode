class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = float('inf')
        count=0
        for i in range(len(nums)):
            if count ==0:
                ele = nums[i]
                count+=1
            elif nums[i]==ele:
                count+=1
            else:
                count-=1
        return -1 if count==0 else ele
        