class Solution(object):
    def countTriples(self, n):
        count = 0 
        for i in range(1,n+1):
            for j in range(1,n+1):
                for k in range(1,n+1):
                    if i*i + j*j == k*k :
                        count+=1
        return count
        
print(Solution().countTriples(5))