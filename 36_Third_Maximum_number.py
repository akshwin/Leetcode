class Solution(object):
    def thirdMax(self, nums):
        nums_set = sorted(set(nums))
        return nums_set[-3] if len(nums_set) >= 3 else nums_set[-1]

print(Solution().thirdMax([3,2,1]))  # 1