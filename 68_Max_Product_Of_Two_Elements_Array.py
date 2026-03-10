class Solution(object):
    def maxProduct(self, nums):
        arr = sorted(nums,reverse=True)
        mx1 = arr[0] - 1 
        mx2 = arr[1] - 1
        
        prod = mx1 * mx2 
        return prod
    
print(Solution().maxProduct([3,4,5,2]))