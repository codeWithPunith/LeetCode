class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minimum = max(weights)
        maximum = sum(weights)
       
        def reqShipsForThisWeight(shipcapacity):
            noofships = 1
            curr=0
            for j in range(len(weights)):
                curr+=weights[j]
                if curr<=shipcapacity:
                    continue
                else:
                    noofships+=1
                    curr = weights[j]
            return noofships
        res=maximum
        while minimum<=maximum:
            
            midWeight = (maximum+minimum)//2
            ships = reqShipsForThisWeight(midWeight)
            
            if ships<=days:
                maximum = midWeight-1
                res = min(res,midWeight)
            else :
                minimum = midWeight+1
        return res

        


        