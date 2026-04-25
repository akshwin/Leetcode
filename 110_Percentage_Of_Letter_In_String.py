class Solution(object):
    def percentageLetter(self, s, letter):
        count = 0 
        for i in s:
            if i == letter:
                count+=1
        return (count * 100 //len(s))

print(Solution().percentageLetter("foobar", "o")) # 33