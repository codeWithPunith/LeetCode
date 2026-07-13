class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n=len(customers)
        customer_satisfied=0
        for i in range(n):
            if grumpy[i]==0:
                customer_satisfied+=customers[i]
        l=0
        r=0
        maximum_window=0
        for r in range(minutes):
            if grumpy[r]:
                maximum_window+=customers[r]
        newmaxima = maximum_window
        while l<n and r<n:
            if grumpy[l]:
                newmaxima-=customers[l]
            l+=1
            r+=1
            if r<n and grumpy[r]:
                newmaxima+=customers[r]

            maximum_window = max(maximum_window,newmaxima)
        return customer_satisfied+maximum_window

