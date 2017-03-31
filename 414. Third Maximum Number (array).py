class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        pay attention to duplicated number
        """
        a = None
        b = None
        c = None
        for i in range(0, len(nums)):
            if a==None or a<nums[i]: 
                c = b
                b = a
                a = nums[i]
            elif a>nums[i]:
                if b<nums[i] or b == None:
                    c = b
                    b = nums[i]
                elif b>nums[i]:
                    if c<nums[i] or c == None:
                        c = nums[i]
        if c==None: return a
        else: return c
