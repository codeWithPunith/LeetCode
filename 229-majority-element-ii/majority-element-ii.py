class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        threshold = len(nums)//3
        res=set()
        for i in range(len(nums)):
            if count[nums[i]]>threshold:
                res.add(nums[i])
        return list(res)

        