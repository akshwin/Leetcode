class Solution(object):
    def countGoodRectangles(self, rectangles):
        maxLen = 0 
        count= 0 

        for w, l in rectangles : 
            side = min (l,w)
            if side > maxLen : 
                maxLen = side
                count = 1 
            elif side == maxLen:
                count+=1
        return count

print(Solution().countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))