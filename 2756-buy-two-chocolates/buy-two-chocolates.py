class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        for i, num in enumerate(prices): 
            if num < prices[1]:
                prices[i], prices[1] = prices[1], prices[i]
                i = 1
            if num < prices[0]: 
                prices[i], prices[0] = prices[0], prices[i]
        
        if prices[0] + prices[1] <= money: 
            return money - prices[0] - prices[1]
        return money