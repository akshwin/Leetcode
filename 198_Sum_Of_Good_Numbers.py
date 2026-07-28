class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        n = len(nums)
        ans = 0 
        for i in range(n):
            good = True 

            if i-k >= 0 and nums[i] <= nums[i-k]:
                good = False
            if i+k <n and nums[i] <= nums[i+k]:
                good = False
            if good : 
                ans +=nums[i]
        return ans

print(Solution().sumOfGoodNumbers([1,2,3,4,5], 1)) # Output: 9