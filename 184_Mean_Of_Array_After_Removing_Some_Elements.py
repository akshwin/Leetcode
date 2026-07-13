class Solution(object):
    def trimMean(self, arr):
        arr.sort()
        n = len(arr)
        k = n // 20
        
        total = 0 
        count = 0 
        for i in range(k,n-k):
            total+=arr[i]
            count+=1
        return float(total)/count
        
print(Solution().trimMean([6,2,7,5,1,2,0,3,10,2,5,0,5,5,6,8,7,6,8,0]))