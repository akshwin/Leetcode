class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        return [i for i in range(1, len(nums) + 1) if i not in nums_set]

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5, 6]