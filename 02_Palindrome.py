class Solution(object):
    def isPalindrome(self, x):
        if x < 0 : 
            return False 
        return str(x) == str(x)[::-1]

print(Solution().isPalindrome(121))  # True
print(Solution().isPalindrome(-121)) # False