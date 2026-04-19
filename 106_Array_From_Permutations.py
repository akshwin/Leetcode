class Solution(object):
    def buildArray(self, nums):
        arr = []
        for i in range(len(nums)):
            arr.append(nums[nums[i]])
        return arr

print(Solution().buildArray([0,2,1,5,3,4]))  # Output