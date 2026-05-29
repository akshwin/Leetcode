class Solution(object):
    def luckyNumbers(self, matrix):
        min_row = [min(row) for row in matrix]

        max_col = [max(col) for col in zip(*matrix)]

        return [num for num in min_row if num in max_col] 
                
print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])) # [15]