class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        cache={}
        n=len(days)
        def helper(i):
            if i in cache:
                return cache[i]
            if i>=n:
                return 0 
            daysItcanPass=0
            val1=helper(i+1)+costs[0]
            daysItcanPass=6+days[i]
            j,k=i,i
            while j<n and days[j]<=daysItcanPass:
                j+=1
            val2=helper(j)+costs[1]
            daysItcanPass=29+days[i]
        
            while k<n and days[k]<=daysItcanPass:
                k+=1
            val3=helper(k)+costs[2]

            min_value= min(val1,val2,val3)
            cache[i]=min_value
            return min_value
        return helper(0)
