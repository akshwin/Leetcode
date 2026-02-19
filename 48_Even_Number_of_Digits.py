class Solution(object):
    def findNumbers(self, nums):
        count = 0 
        for num in nums : 
            num_str =str(num) 
            if len(num_str)% 2  == 0 : 
                count +=1
        return count

print(Solution().findNumbers([12,345,23,6,7896]))