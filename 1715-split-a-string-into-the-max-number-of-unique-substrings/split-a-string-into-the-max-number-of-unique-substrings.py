class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #the approach can be something like this take a ele and check in set if its unique or not 
        # substrings = set()
        # def backTracking(s,i):
        #     if i>=len(s):
        #         return
        #     sub =s[i]
        #     if sub not in substrings:
        #         substrings.add(sub)
        #     else:
        #         while i+1<len(s) and sub in substrings:
        #             sub+=s[i+1]
        #             i+=1
        #         substrings.add(sub)

        #     backTracking(s,i+1)
        # backTracking(s,0)
        # print(substrings)
        # return len(substrings)
        #the above greedy one doesnt pass few test cases
        cur_set = set()
        
        def bt(i,cur_set):
            if i==len(s):
                return 0
            res=0
            for j in range(i,len(s)):
                sub = s[i:j+1] 
                if sub in cur_set:
                    continue
                cur_set.add(sub)
                res = max(1+bt(j+1,cur_set),res)
                cur_set.remove(sub)
            return res
        return bt(0,set())