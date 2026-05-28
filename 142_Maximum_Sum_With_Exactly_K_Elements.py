class Solution(object):
    def maximizeSum(self, nums, k):
        score = 0 

        for i in range(k):
            mx = max(nums)
            score+=mx
            nums.remove(mx)
            nums.append(mx+1)
        return score

print(Solution().maximizeSum([1,2,3,4,5], 3)) # 18