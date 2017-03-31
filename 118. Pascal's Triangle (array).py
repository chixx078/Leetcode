class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        
        set result list first to avoid index out of range
        """
        result = []
        for i in range(0,numRows):
            result.append([1]*(i+1))
            
        for i in range(0,numRows):
            for j in range(1,i):
                result[i][j] = result[i-1][j-1]+ result[i-1][j]
        return result
