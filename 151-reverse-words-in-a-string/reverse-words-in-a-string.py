class Solution:
    def reverseWords(self, s: str) -> str:
        stk=[]
        i=0
        while i<len(s):
            while i<len(s) and s[i]==" ":
                i+=1
            ele=""
            while i<len(s) and s[i]!=" ":
                ele+=s[i]
                i+=1
            if ele:
                stk.append(ele)
            
        res=""
        while len(stk)!=1:
            ele = stk.pop()
            res+=ele+" "
        res+=stk.pop()
        return res
        