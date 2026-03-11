class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for i in arr1:
            for j in arr2:
                valid = True
                if abs(i-j)<=d:
                    valid = False
                    break
            if valid:
                count+=1
        return count
                
print(Solution().findTheDistanceValue([4,5,8], [10,9,1,8], 2))