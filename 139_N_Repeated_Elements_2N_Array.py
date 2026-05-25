from collections import Counter
class Solution(object):
    def repeatedNTimes(self, nums):
        length = len(nums)//2
        counter = Counter ()
        
        for num in nums:
            counter[num] +=1
        
        for key , value in counter.items():
            if value == length:
                return key

print(Solution().repeatedNTimes([1,2,3,3]))