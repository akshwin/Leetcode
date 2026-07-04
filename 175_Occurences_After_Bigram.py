class Solution(object):
    def findOcurrences(self, text, first, second):
        result = []
        words = text.split()
        
        for i in range(len(words)-2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        return result

print(Solution().findOcurrences("alice is a good girl and she is a good student", "a", "good"))