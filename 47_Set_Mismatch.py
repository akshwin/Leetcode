class Solution(object):
    def findErrorNums(self, nums):
        seen = set()
        duplicate = -1
        
        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
        
        n = len(nums)
        total = n * (n + 1) // 2
        missing = total - (sum(nums) - duplicate)
        
        return [duplicate, missing]

print(Solution().findErrorNums([1,2,2,4]))