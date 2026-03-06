class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        
        for i in range(n - n//4):
            if arr[i] == arr[i + n//4]:
                return arr[i]

print(Solution().findSpecialInteger([1,2,3,3])) # 3