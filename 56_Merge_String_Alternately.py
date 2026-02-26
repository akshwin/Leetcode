class Solution(object):
    def mergeAlternately(self, word1, word2):
        merge = []
        i = 0
        while i < len(word1) and i < len(word2):
            merge.append(word1[i])
            merge.append(word2[i])
            i += 1
        merge.append(word1[i:])
        merge.append(word2[i:])
        return "".join(merge)
        
print(Solution().mergeAlternately("abc", "pqr"))  # Output: "apbqcr"