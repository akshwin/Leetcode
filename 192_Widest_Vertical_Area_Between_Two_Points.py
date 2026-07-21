class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        x = sorted(points[0] for point in points)
        
        ans = 0 
        for i in range(1,len(x)):
            ans = max(ans,x[i] - x[i-1])
        return ans 
    
print(Solution().maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))