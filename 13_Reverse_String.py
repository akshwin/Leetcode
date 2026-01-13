class Solution(object):
    def reverseString(self, s):
        s[:] = s[::-1]
        return s 
            
print(Solution().reverseString(["h","e","l","l","o"]))