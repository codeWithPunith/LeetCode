class Solution:
    def sumAndMultiply(self, n: int) -> int:
        #while looop to remove zero
        copy = n
        res1=0
        mysum=0
        while copy:
            digit=copy%10
            if digit!=0:
                res1=res1*10+digit
                mysum+=digit
            copy=copy//10
        res2=0
        while res1:
            digit = res1%10
            res2=res2*10+digit
            res1=res1//10
        return res2*mysum
