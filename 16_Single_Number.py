class Solution(object):
    def singleNumber(self, nums):
        result = 0 
        for num in nums:
            result^=num
        return result
        
print(Solution().singleNumber([4,1,2,1,2]))  # 4