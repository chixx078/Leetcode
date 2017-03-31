class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        minnow: min element so far
        maxdiff: maxdifference so far
        """
        minnow = None
        maxdiff = 0
        diff = 0
        for i in range(0, len(prices)):
            if prices[i]<minnow or minnow==None:
                minnow = prices[i]
            diff = prices[i] - minnow
            if diff > maxdiff :
                maxdiff = diff
        return maxdiff
