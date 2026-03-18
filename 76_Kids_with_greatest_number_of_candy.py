class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        result = []

        for c in candies : 
            if c+extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result        

print(Solution().kidsWithCandies([2,3,5,1,3], 3))