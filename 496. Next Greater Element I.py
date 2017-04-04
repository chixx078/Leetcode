class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for j in range (len(findNums)):
            for i in range(nums.index(findNums[j]),len(nums)):
                if nums[i]>findNums[j]:
                    result.append(nums[i])
                    break
            if len(result)==j:
                result.append(-1)
        return result
