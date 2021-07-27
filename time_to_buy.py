class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_stock = min(prices)
        min_index = prices.index(min_stock)
        #print(min_stock, prices.index(min_stock),len(prices))
        if prices.index(min_stock) >= len(prices)-1:
            print(prices.index(min_stock),len(prices))
            return 0
        else:
            new_stock_price = prices[min_index:]
         #   print(new_stock_price)
            max_stock = max(new_stock_price)
            return (abs(min_stock - max_stock))
        
