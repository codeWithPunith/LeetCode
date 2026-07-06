class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #bruteforce 
        res=0
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
        return res