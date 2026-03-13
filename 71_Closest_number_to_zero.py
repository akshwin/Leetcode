class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]

        for num in nums:
            if abs(num)<abs(closest):
                closest = num
            elif abs(num) == abs(closest) and num>closest:
                closest = num
        return closest        
        
print(Solution().findClosestNumber([-4,-2,1,4,8]))