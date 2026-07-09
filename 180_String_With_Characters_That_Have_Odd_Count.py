class Solution(object):
    def generateTheString(self, n):
        if n % 2 == 1:
            return n * 'a'
        else:
            return (n-1) * 'a' + "b"
        
print(Solution().generateTheString(4))  # Output: "aaab"