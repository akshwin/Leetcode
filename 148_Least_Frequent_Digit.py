from collections import Counter
class Solution(object):
    def getLeastFrequentDigit(self, n):
        counter = Counter(str(n))
        min_freq = min(counter.values())

        return min(int(d) for d ,f in counter.items() if f == min_freq)
        
print(Solution().getLeastFrequentDigit(123321)) # 1