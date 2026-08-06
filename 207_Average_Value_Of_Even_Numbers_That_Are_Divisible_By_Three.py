class Solution(object):
    def averageValue(self, nums):
        total = 0 
        total_sum = 0 
        for i in nums:
            if i % 2 == 0 and i % 3 == 0 : 
                total +=1
                total_sum+=i
            
        if total == 0 :
            return 0
        
        return total_sum//total
        
print(Solution().averageValue([1,3,6,10,12,15])) # 9