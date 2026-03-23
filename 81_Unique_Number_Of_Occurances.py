class Solution(object):
    def uniqueOccurrences(self, arr):
        from collections import Counter
        counts = Counter(arr).values()
        return len(counts) == len(set(counts))
        
print(Solution().uniqueOccurrences([1,2,2,1,1,3]))