class Solution(object):
    def maxProductDifference(self, nums):
        n = len(nums)
        nums = sorted(nums)
        prod = (nums[-1] * nums[-2]) - (nums[0] * nums[1])
        return prod

print(Solution().maxProductDifference([5,6,2,7,4]))  # Output: 34