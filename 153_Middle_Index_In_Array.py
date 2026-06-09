class Solution(object):
    def findMiddleIndex(self, nums):
        totalSum = sum(nums)
        leftSum = 0 

        for i in range(len(nums)):
            rightSum = totalSum - leftSum - nums[i]

            if leftSum == rightSum :
                return i 

            leftSum +=nums[i]
        return -1
        
print(Solution().findMiddleIndex([2, 3, -1, 8, 4])) # 3