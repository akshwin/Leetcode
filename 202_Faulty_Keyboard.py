class Solution(object):
    def finalString(self, s):
        ans = ""
        
        for ch in s : 
            if ch == 'i':
                ans = ans[::-1]
            else:
                ans +=ch
        return ans

print(Solution().finalString("string")) 