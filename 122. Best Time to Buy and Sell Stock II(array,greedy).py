class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        Input: [7, 1, 5, 3, 6, 4]
        """
        if len(prices)==0 or len(prices)==1 : return 0
        result = 0
        buy = prices[0]
        sell = prices[1]
        
        for i in range (0,len(prices)-1):
            buy = prices[i]
            sell = prices[i+1]
            if(sell-buy > 0):
                result += sell-buy
                
        return result
