class Solution(object):
    def arraySign(self, nums):
        prod = 1 
        for i in nums :
            prod *=i

        if prod >0 : 
            return 1 
        elif prod <0:
            return -1
        else:
            return 0 

print(Solution().arraySign([-1,-2,-3,-4,3,2,1]))