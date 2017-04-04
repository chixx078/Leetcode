class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        result = 0
        for c in s:
            dic[c] = dic.get(c,0)+1
        
        odd = False
        for key in dic:
            if dic[key]%2 == 0:
                result += dic[key]
            else:
                result += dic[key]-1
                odd = True
        
        if odd:
            result+=1
        return result
