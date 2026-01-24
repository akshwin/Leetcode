class Solution(object):
    def findLucky(self, arr):
        from collections import Counter
        freq = Counter(arr)
        ans = -1 

        for num , freq in freq.items():
            if num == freq:
                ans = max(ans,num)
        return ans

print(Solution().findLucky([2,2,3,4]))  # Output: 2