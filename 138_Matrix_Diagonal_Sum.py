class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        sum = 0 
        for i in range(n):
            sum+=mat[i][i]

            if i != n - 1 - i :
                sum+=mat[i][n-1-i]
        return sum
        
print(Solution().diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))