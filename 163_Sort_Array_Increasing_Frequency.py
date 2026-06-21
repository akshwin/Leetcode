from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        count = Counter(nums)
        nums.sort(key = lambda x:(count[x],-x))
        
        return nums
print(Solution().frequencySort([1,1,2,2,2,3]))  # Output: [3,1,1,2,2,2]