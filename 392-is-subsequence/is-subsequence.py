class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #check s is subseq of t not t is of s
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i==len(s)