class Solution(object):
    def freqAlphabets(self, s):
        res = s
        
        for i in range(10, 27):
            res = res.replace(str(i) + "#", chr(ord('a') + i - 1))
            
        for i in range(1, 10):
            res = res.replace(str(i), chr(ord('a') + i - 1))
        
        return res
    
print(Solution().freqAlphabets("10#11#12"))