class Solution(object):
    def getMinDistance(self, nums, target, start):
        ans = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                ans = min(ans,abs(i-start))
        return ans
        
print(Solution().getMinDistance([1,2,3,4,5], 5, 3))