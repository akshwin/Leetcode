class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        
        def word_to_number(word):
            num = ""

            for ch in word:
                num+=str(ord(ch)-ord('a'))
            return int(num)
        
        return (word_to_number(firstWord)+word_to_number(secondWord) == word_to_number(targetWord))
        
print(Solution().isSumEqual("acb", "cba", "cdb"))