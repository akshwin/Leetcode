class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in result:
                result.append(nums1[i])
        return result

print(Solution().intersection([1, 2, 2, 1,3,4], [2, 2,3,41]))  # Output: [2]