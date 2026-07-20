
class Solution(object):
    def largestGoodInteger(self, num):
        ans = ""

        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                candidate = num[i:i+3]
                ans = max(ans,candidate)
        return ans
        
print(Solution().largestGoodInteger("6777133339"))  # Output: "777"