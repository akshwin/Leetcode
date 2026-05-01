class Solution(object):
    def findMissingElements(self, nums):
        s = set(nums)
        mn, mx = min(nums), max(nums)
        
        result = []
        for x in range(mn, mx + 1):
            if x not in s:
                result.append(x)
        
        return result

print(Solution().findMissingElements([1, 3, 5, 7, 9]))  # Output: [2, 4, 6, 8]