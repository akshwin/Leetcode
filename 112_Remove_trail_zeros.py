class Solution(object):
    def removeTrailingZeros(self, num):
        return num.rstrip('0')

print(Solution().removeTrailingZeros("34500"))