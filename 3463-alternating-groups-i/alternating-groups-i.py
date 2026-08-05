class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        r,l=2,0
        n=len(colors)
        alternating=0
        def isValid(l,r):
            if colors[l%n]==colors[r%n] and colors[l%n]!=colors[(l+1)%n]:
                return True
            return False
       
        while l<n:
            if isValid(l,r):
                alternating+=1
            l+=1
            r+=1
        return alternating
            
        
        