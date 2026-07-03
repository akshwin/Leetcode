from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        result = []
        counter = Counter(s1.split()+s2.split())

        for word, freq in counter.items():
            if freq == 1:
                result.append(word)
        return result
    
print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))