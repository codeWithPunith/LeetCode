class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 0
        def dfs(alphabets,pasting):
            if alphabets==n:
                return 0
            if alphabets>n:
                return 1000
            res1 = 1+dfs(alphabets+pasting,pasting)
            res2 = 2+dfs(alphabets+alphabets,alphabets)
            return min(res1,res2)
        return dfs(1,1)+1