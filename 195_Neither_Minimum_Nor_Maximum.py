class Solution(object):
    def findNonMinOrMax(self, nums):
        for i in nums:
            if i != max(nums) and i != min(nums):
                return i 
        return -1 
        
print(Solution().findNonMinOrMax([3, 2, 1, 4])) # Output: 2