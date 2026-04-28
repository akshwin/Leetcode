class Solution(object):
    def largestEven(self, s):
        idx = s.rfind("2")
        return s[:idx+1] if idx != -1 else ""


print(Solution().largestEven("52"))  # Output: "52"