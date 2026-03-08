class Solution(object):
    def dominantIndex(self, nums):
        sorted_nums = sorted(nums, reverse=True)
        
        if sorted_nums[0] >= 2 * sorted_nums[1]:
            return nums.index(sorted_nums[0])
        
        return -1


print(Solution().dominantIndex([3, 6, 1, 0]))