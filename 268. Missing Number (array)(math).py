class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        exp = (n+1)*n/2
        
        for i in range(0,len(nums)):
            exp -= nums[i]
            
        return exp
