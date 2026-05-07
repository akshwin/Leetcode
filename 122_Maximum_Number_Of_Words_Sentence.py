class Solution(object):
    def mostWordsFound(self, sentences):
        max = 0 
        for sentence in sentences:
            word_count = len(sentence.split())
            if word_count>max:
                max = word_count
        return max

print(Solution().mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))