class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxRange = float('-inf')
        maxSum=0
        for i,n in enumerate(nums):
            small = float('inf')
            large = float('-inf')
            while n :
                digit = n%10
                small = min(digit,small)
                large = max(digit,large)
                n=n//10
            if large-small >=maxRange:
                if maxRange ==large-small:
                    maxSum += nums[i]
                    continue
                maxRange = large-small
                maxSum = nums[i]
        return maxSum
                


        