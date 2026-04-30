class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = 0 
        num2 = 0 

        for i in range(n+1):
            if i % m == 0 : 
                num2+=i
            else:
                num1+=i
        return num1-num2

print(Solution().differenceOfSums(10, 3))