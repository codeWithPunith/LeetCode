class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        #genral approach is add fruit and then validate the window
        l,r,total =0,0,0
        count = defaultdict(int)
        res=0
        while r<len(fruits):
            count[fruits[r]]+=1
            total+=1
            r+=1
            while len(count)>2:
                fruit = fruits[l]
                count[fruit]-=1
                total-=1
                l+=1
                if count[fruit]==0:
                    count.pop(fruit)
            res = max(res,total)
        return res

        