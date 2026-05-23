class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        broken = set(brokenLetters)
        count = 0 

        for word in text.split():
            can_type = True 

            for ch in word:
                if ch in broken:
                    can_type = False
                    break
            if can_type :
                count+=1
        return count 
        
print(Solution().canBeTypedWords("hello world", "ad")) # 1