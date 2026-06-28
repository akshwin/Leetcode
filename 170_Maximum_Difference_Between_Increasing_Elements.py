class Solution(object):
    def maximumDifference(self, nums):
        diff = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    diff = max(diff,nums[j] - nums[i])
        return diff        
    
print(Solution().maximumDifference([7,1,5,4]))