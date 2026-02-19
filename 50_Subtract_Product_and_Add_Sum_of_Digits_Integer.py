class Solution(object):
    def subtractProductAndSum(self, n):
        prod = 1 
        sum = 0 
        n_str = str(n)
        for i in n_str:
            i = int(i)
            prod = prod*i
            sum +=i
        return prod-sum
    
print(Solution().subtractProductAndSum(4421))