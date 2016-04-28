class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        currMin = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            currMin = min(currMin, prices[i])
            maxProfit = max(maxProfit, prices[i] - currMin)
        return maxProfit