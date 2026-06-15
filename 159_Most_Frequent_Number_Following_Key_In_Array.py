from collections import Counter
class Solution(object):
    def mostFrequent(self, nums, key):
            counter = Counter(nums[i+1] for i in range(len(nums) - 1) if nums[i] == key)
            return counter.most_common(1)[0][0]
        
print(Solution().mostFrequent([1,100,200,1,100], 1))  # Output: 100