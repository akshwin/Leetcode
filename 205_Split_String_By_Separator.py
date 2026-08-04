class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        ans = []

        for word in words:
            parts = word.split(separator)
            for part in parts:
                if part:
                    ans.append(part)
        return ans
        
print(Solution().splitWordsBySeparator(["one.two.three","four.five","six"], "."))