class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """"the solution is easy when u sort the intervals it makes sure that every start will be greater or equal to the previous start ie you will always get a greater start interval, so all u need to check is if the current end is greater than the previous end if its greater then there is no merge if not the interval is merged """
        intervals.sort(key = lambda x : (x[0],-x[1]))
        maxend=0
        res=0
        for s,e in intervals:
            if e>maxend:
                maxend =e
                res+=1
        return res
       
        
        
        
        
        
        
        """
        #bruteforce 
        res=0
        arr=[]
        for i,interval in enumerate(intervals):
            start=interval[0]
            end = interval[1]
            iscovered = False
            for j in range(len(intervals)):
                if i==j:
                    continue
                if intervals[j][0]<=start and end<=intervals[j][1]:
                    iscovered= True
            if not iscovered:
                res+=1
                arr.append([start,end])
        print(arr)
        return res
        """

        