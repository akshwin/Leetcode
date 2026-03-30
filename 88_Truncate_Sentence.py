class Solution(object):
    def truncateSentence(self, s, k):
        s = s.split()
        return " ".join(s[:k])

s = "Hello how are you Contestant"
k = 4   
print(Solution().truncateSentence(s, k))
            
            
        