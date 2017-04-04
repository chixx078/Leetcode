class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #using list to implememt stack
        dic = {"(":")","[":"]","{":"}"}
        
        for c in s:
            if c in dic: #if c is a key in dictionary
                stack.append(c)
            else:
                if stack ==[]:
                    return False
                elif dic[stack.pop()] != c:
                    return False
        return stack==[]
        
