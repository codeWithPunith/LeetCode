class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        ele=[1]
        res.append(ele)
        if numRows==1:
            return res
        res.append((1,1))
        if numRows==2:
            return res
        for i in range(2,numRows):
            arr=[]
            arr.append(1)
            for j in range(len(res)-1):
                arr.append(res[i-1][j]+res[i-1][j+1])
            arr.append(1)
            res.append(arr)
        return res
        