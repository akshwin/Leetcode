class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected = (n*(n+1))//2
        result = expected - sum(nums)
        return result
            
print(Solution().missingNumber([3,0,1]))