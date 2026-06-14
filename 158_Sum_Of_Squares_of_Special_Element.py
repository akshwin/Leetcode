class Solution(object):
    def sumOfSquares(self, nums):
        sum = 0 
        n = len(nums)

        for i in range(n):
            if n % (i+1) == 0 :
                square = nums[i] * nums[i]
                sum +=square
        return sum

print(Solution().sumOfSquares([1, 2, 3, 4, 5, 6]))