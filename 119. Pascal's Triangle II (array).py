class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        
        add backward or we will have [1,3,*4,1]
        """
        result = [1]*(rowIndex+1)
        for i in range(0,rowIndex+1):
            for j in range(i-1, 0,-1):
                result[j] += result[j-1]
        return result
