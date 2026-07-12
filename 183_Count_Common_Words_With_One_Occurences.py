from collections import Counter
class Solution(object):
    def countWords(self, words1, words2):
        counter = Counter(words1+words2)
        count = 0 
        for num, freq in counter.items():
            if freq == 2:
                count+=1
        return count
    
print(Solution().countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))