class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        unsorted array, two pointers, changable order
        
        Starting from the left every time we find a value that is the target value we swap it out with an item starting from the right. We decrement end each time as we know that the final item is the target value and only increment start once we know the value is ok. Once start reaches end we know all items after that point are the target value so we can stop there.
        """
        if len(nums)==0:
            return 0
        
        start = 0
        end = len(nums)-1
        
        while start<=end:
            if nums[start]==val:
                nums[start],nums[end]=nums[end],nums[start]
                end-=1
            else:
                start+=1
        return start
