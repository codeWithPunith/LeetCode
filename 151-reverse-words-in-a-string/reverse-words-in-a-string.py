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
            
       
        return " ".join(stk[::-1])