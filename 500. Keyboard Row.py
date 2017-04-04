class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        
        set: http://blog.csdn.net/business122/article/details/7541486
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        
        for word in words:
            t = set(word.lower())
            if t&row1==t or t&row2==t or t&row3==t:
                result.append(word)
        return result
