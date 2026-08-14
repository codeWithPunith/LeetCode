class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False

        allMightyString = "".join([s,s])
        i=0
        j=0
        goalIterator =0
        while j < len(allMightyString):
            if j-i == len(goal):
                return True
            if allMightyString[j] ==goal[goalIterator]:
                j+=1
                goalIterator+=1
            else:
                i+=1
                j=i
                goalIterator=0
        return False
        