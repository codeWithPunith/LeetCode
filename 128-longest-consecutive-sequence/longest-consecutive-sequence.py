class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        res =0
        dic=defaultdict(int)
        for n in set_of_nums:
            curRes=1
            ele =n-1
            while ele in set_of_nums:
                if dic[ele]!=0:
                    curRes+=dic[ele]
                    break
                curRes+=1
                ele-=1
            dic[n]=curRes
            res = max(res,curRes)
        return res


        