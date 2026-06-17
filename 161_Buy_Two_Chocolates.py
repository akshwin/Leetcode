class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()

        cost = prices[0] + prices[1] 

        if cost <= money : 
            return money-cost
        
        return money

print(Solution().buyChoco([1,2,2], 3)) # 0