from collections import Counter
class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        count = Counter()

        for num in set(nums1):
            count[num] +=1
        for num in set(nums2):
            count[num] +=1
        for num in set(nums3):
            count[num] +=1

        return [ num for num , freq in count.items() if freq >=2 ]
        

print(Solution().twoOutOfThree([1,1,3,2], [2,3], [3]))