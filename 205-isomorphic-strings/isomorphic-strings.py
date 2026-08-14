class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map={}
        map2={}
        for sc,tc in zip(s,t):
            if sc in map and map[sc]!=tc:
                return False
            if tc in map2 and map2[tc]!=sc:
                return False
            map[sc]=tc
            map2[tc]=sc
        return True                

                
        