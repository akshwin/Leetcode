class Solution(object):
    def findWordsContaining(self, words, x):
        res = []
        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res
        
print(Solution().findWordsContaining(["hello", "world", "leetcode"], 'o'))  # Output: [0, 1]