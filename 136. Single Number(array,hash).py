class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range (0, len(nums)):
            if(nums[i] in dic):
                del dic[nums[i]] 
            else:
                dic[nums[i]] = 1
        for key in dic:
            return key
