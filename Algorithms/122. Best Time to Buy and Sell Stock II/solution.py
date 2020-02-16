class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        currMin = prices[0]
        currPrice = prices[0]
        isIncrese = False
        profit  = 0
        for i in range(len(prices)-1):
            
            if prices[i] <= prices[i+1]:
                currPrice = prices[i+1]
                isIncrese = True
            else:
                if isIncrese:
                    profit += currPrice- currMin
                isIncrese = False    
                currMin = prices[i+1]
        if isIncrese:
            profit += currPrice - currMin
        return profit