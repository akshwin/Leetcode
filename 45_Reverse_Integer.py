class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ") 
        
        para = paragraph.lower().split()
        
        word_count = {}
        for word in para:
            if word not in banned:
                word_count[word] = word_count.get(word, 0) + 1

        most_common = max(word_count, key=word_count.get)
        return most_common
    

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))