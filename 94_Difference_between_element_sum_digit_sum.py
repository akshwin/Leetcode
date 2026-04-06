class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = 0 
        digit_sum = 0 
        for i in nums: 
            element_sum+=i
        for num in nums:
            for digits in str(num):
                digit_sum +=int(digits)
        return abs(element_sum-digit_sum)

print(Solution().differenceOfSum([1,15,6,3]))