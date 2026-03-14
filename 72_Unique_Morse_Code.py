class Solution(object):
    def uniqueMorseRepresentations(self,words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                "..-","...-",".--","-..-","-.--","--.."]

        transformations = []

        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - 97]

            if code not in transformations:
                transformations.append(code)

        return len(transformations)

print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))