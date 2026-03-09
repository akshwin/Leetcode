class Solution(object):
    def findGCD(self, nums):
        mx = max(nums)
        mn = min(nums)

        for i in range(mn,0,-1):
            if mn % i  == 0 and mx % i  == 0 :
                return i

print(Solution().findGCD([2,5,6,9,10]))