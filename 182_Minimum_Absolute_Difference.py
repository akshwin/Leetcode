class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        result = []
        min_diff = float('inf')

        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff<min_diff:
                min_diff = diff
        
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i],arr[i+1]])

        return result
    
print(Solution().minimumAbsDifference([4,2,1,3]))