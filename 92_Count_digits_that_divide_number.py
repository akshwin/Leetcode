class Solution(object):
    def countDigits(self, num):
        count = 0 
        num = str(num)
        for i in num : 
            if int(num)%int(i) == 0 :
                count+=1
        return count

print(Solution().countDigits(1248))