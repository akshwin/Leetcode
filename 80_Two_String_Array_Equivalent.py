class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        print("".join(word1))
        print("".join(word2))

        if "".join(word1) == "".join(word2):
            return True
        else:
            return False
        
print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"])) # True