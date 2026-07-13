class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #characters needed to be appended to the s not t where is the sequence
        i,j=0,0   # j cant be moved without matching character at j
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                j+=1
            i+=1
        return len(t)-j