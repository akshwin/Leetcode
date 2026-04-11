class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            num = nums[i]
            if i == sum(int(d) for d in str(num)):
                return i 
        return -1

print(Solution().smallestIndex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) # Output: 0