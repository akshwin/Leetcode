class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        count = 0 
        for i in range(len(heights)):
            if expected[i] == heights[i]:
                count+=1
        return len(heights) - count
        
print(Solution().heightChecker([1,1,4,2,1,3]))