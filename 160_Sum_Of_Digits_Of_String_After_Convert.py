class Solution(object):
    def getLucky(self, s, k):
        num = "".join(str(ord(ch) - ord('a') + 1) for ch in s)

        for i in range(k):
            num = str(sum(int(d) for d in num))

        return int(num)
    
print(Solution().getLucky("leetcode", 2))  # Output: 6