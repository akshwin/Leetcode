class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        while num >= 10:
            num = sum(int(digit) for digit in str(num))
        return num
    
print(Solution().addDigits(38))  # 2