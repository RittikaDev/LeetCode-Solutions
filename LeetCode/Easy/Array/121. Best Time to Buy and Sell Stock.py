from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit




# EXAMPLE USAGE
if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    result = sol.maxProfit(prices)
    print(result)