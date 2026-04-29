class Solution(object):
    def canAliceWin(self, nums):
        single = 0 
        double = 0 

        for i in nums:
            if i <10:
                single+=i
            elif i<100:
                double+=i
        
        total = sum(nums)

        return (single> (total-single)) or (double > (total- double))
        
print(Solution().canAliceWin([1, 2, 3, 4, 5, 6, 7, 8, 9]))