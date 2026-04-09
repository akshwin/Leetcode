class Solution(object):
    def getSneakyNumbers(self, nums):
        n = len(nums)
        freq = [0] * n
        res = []
        for num in nums:
            freq[num]+=1
            if freq[num] == 2:
                res.append(num)
        return res

print(Solution().getSneakyNumbers([1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10, 1]))