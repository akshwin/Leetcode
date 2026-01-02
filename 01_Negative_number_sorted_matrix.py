class Solution(object):
    def countNegatives(self, grid):
        def countNegativesinrows(row):
            left, right = 0, len(row)

            while left < right:
                mid = (left + right) // 2

                if row[mid] < 0:
                    right = mid
                else:
                    left = mid + 1

            return len(row) - left

        total_neg = 0
        for row in grid:
            total_neg += countNegativesinrows(row)

        return total_neg

print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))  # 8

