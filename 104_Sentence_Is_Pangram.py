class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26

print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))