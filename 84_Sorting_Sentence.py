class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        res = [""] * len(words)
        for w in words:
            pos = int(w[-1])-1
            res[pos]  = w[:-1]
        
        return " ".join(res)

print(Solution().sortSentence("is2 sentence4 This1 a3")) # This is a sentence