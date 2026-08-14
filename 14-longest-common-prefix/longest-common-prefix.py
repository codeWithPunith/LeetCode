class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        commonPrefix= strs[0]
        for i in range(1,len(strs)):
            s2 = strs[i]
            index1,index2 = 0,0
            while index1<len(commonPrefix) and index2<len(s2) and commonPrefix[index1]==s2[index2]:
                index1+=1
                index2+=1
            commonPrefix=commonPrefix[:index1]
        return commonPrefix

        