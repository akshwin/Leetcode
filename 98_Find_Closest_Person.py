class Solution(object):
    def findClosest(self, x, y, z):
        if abs(x-z) > abs(y-z):
            return 2
        elif abs(x-z) == abs(y-z):
            return 0
        else:
            return 1 
        
print(Solution().findClosest(1, 2, 3))