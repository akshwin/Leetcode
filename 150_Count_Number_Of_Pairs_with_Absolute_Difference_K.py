class Solution(object):
    def countKDifference(self, nums, k):
        n = len(nums)
        count = 0 
        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j]) == k:
                    count+=1
        return count

print(Solution().countKDifference([1,2,2,1], 1))