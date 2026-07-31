class Solution(object):
    def maxPower(self, s):
        max_power = 1 
        current = 1 

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                current+=1
            else:
                current=1
            max_power = max(max_power,current)
        
        return max_power
    
print(Solution().maxPower("leetcode")) # Output: 2