class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        count = 0 
        seen = set()

        for word in words:
            rev = word[::-1]

            if rev in seen:
                count+=1
            else:
                seen.add(word)
        return count
        
print(Solution().maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"]))