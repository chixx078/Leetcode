class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        base case:
        f(0) = 0
        f(1) = nums[0]
        f(2) = max(nums[0], nums[1])
        
        function:
        f(n) = max(f(n-1), f(n-2)+ money in the nth house)
             = max(f(n-1), f(n-2) + nums[n-1])
        """
        """
        recursive - top-down
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        if n==2: return max(nums[0],nums[1])
        
        sub1 = self.rob(nums[:n-1])
        sub2 = self.rob(nums[:n-2])
        return max(sub1, sub2 + nums[n-1])
        """
        """
        DP - O(n) time and space
        
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        dp = [0]*(n+1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        
        return dp[n]
        """
        """
        optimization - we don't need to store each f(i) in dp array
        use pre, cur to store f(n-2) and f(n-1) -> O(n) time O(1) space
        """
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        pre = 0
        cur = 0
        temp = -1
        for i in range(0, n):
            temp = cur
            cur = max(cur, pre+nums[i])
            pre = temp
            
        return cur
        
        
        
