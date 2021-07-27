class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_stock = min(prices)
        if prices.index(min_stock) >= len(prices):
            return 0
        else:
            new_stock_price = prices[min_stock:]
            max_stock = max(new_stock_price)
            return (abs(min_stock - max_stock))
        
