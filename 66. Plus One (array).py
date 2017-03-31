class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        129
        99
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1 
            else:
                digits[i] = 0
            
            if digits[i] != 0:
                return digits
        
        digits.insert(0,1)
        return digits
