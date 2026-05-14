class Solution(object):
    def isAcronym(self, words, s):
        ac = ""
        for word in words:
            ac+=word[0]
        
        return ac == s
    
print(Solution().isAcronym(["alice","bob","charlie"], "abc"))