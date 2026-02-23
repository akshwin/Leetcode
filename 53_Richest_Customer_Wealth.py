class Solution(object):
    def maximumWealth(self, accounts):
        max_sum = 0
        for i in range(len(accounts)):
            if max_sum < sum(accounts[i]):
                max_sum = sum(accounts[i])
        return max_sum

print(Solution().maximumWealth([[1,2,3],[3,2,1]]))