class Solution(object):
    def makeFancyString(self, s):
        ans = []
        for ch in s: 
            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch : 
                continue
            ans.append(ch)
        return "".join(ans) 
    
print(Solution().makeFancyString("leeetcode")) # Output: "leetcode"