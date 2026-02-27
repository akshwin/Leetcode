class Solution(object):
    def intersection(self, nums):
        common = set(nums[0])
        for arr in nums[1:]:
            common &= set(arr)
        return sorted(common)

print(Solution().intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))