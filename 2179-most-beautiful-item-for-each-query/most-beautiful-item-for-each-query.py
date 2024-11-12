class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort()

        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])
        
        prices = [price for price, _ in items]
        output = []


        for price in queries:
            target_index = bisect_right(prices, price)
            output.append(0 if target_index == 0 else items[target_index - 1][1])
        
        return output



        """
items[i] = [price_i, beuatiy_i]

queries[j] to find max beauty of item whose price is less than or equal to queries[j]

this feels like a sort by price
then do a prefix for max beauty
rolling max beauty 
        """
        