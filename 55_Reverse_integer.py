class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        x = list(str(x))
        x.reverse()
        
        rev = int("".join(x))
        rev *= sign
        
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev
    
print(Solution().reverse(-123))