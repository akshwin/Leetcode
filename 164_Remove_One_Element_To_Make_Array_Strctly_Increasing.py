class Solution(object):
    def canBeIncreasing(self, nums):
        def increasing(arr):
            for i in range(1,len(arr)):
                if arr[i] <= arr[i-1]:
                    return False
            return True

        if increasing(nums):
            return True
            
        for i in range(len(nums)):
            if increasing(nums[:i]+nums[i+1:]):
                return True
        return False
        
print(Solution().canBeIncreasing([1,2,10,5,7])) # True