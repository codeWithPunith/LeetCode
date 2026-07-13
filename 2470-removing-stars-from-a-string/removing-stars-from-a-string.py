class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk=[]
        for c in s:
            if c=='*' and stk:
                stk.pop()
            else:
                stk.append(c)
        
        return "".join(stk)
        