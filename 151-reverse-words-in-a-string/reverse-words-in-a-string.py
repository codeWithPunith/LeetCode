class Solution:
    def reverseWords(self, s: str) -> str:
        sb = collections.deque()
        i=0
        while i<len(s):
            while i<len(s) and s[i]==" ":
                i+=1
            start=i
            while i<len(s) and s[i]!=" ":
                i+=1
            if s[start:i]:
                sb.appendleft(s[start:i])
            
       
        return " ".join(sb)