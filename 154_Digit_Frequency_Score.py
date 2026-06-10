from collections import Counter
class Solution(object):
    def digitFrequencyScore(self, n):
        score = 0 
        counter = Counter(str(n))
        
        for digit , freq in counter.items():
            score += int(digit) * freq
        
        return score

print(Solution().digitFrequencyScore(123321)) # 12