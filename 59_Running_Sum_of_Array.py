class Solution(object):
    def runningSum(self, nums):
        result = []
        sum = 0 
        for i in range(len(nums)):
            sum +=nums[i]
            result.append(sum)            
        return result
            

print(Solution().runningSum([1,2,3,4]))