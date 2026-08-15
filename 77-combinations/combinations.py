class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        superSet=[]
        def helper(currentNumber,currentCombination):
            if len(currentCombination)==k:
                superSet.append(currentCombination[:])
                return 

            if currentNumber>n:
                return 
        
            helper(currentNumber+1,currentCombination)
            currentCombination.append(currentNumber)
            helper(currentNumber+1,currentCombination)
            currentCombination.pop()
            return 
        helper(1,[])
        return superSet
        

        