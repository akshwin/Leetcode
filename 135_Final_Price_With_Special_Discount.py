class Solution(object):
    def finalPrices(self, prices):
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices
    
print(Solution().finalPrices([8, 4, 6, 2, 3]))