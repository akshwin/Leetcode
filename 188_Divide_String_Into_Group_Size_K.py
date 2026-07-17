class Solution(object):
    def divideString(self, s, k, fill):
        ans = []

        for i in range(0,len(s),k):
            group = s[i:i+k]
            if len(group) <k:
                group +=fill * (k- len(group)) 
            ans.append(group)
        return ans 
        
print(Solution().divideString("abcdefghij", 3, "x")) # Output: ['abc', 'def', 'ghi', 'jxx']