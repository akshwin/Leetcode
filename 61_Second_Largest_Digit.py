class Solution(object):
    def secondHighest(self, s):
        digits = set()
        
        for char in s:
            if char.isdigit():
                digits.add(int(char))
        
        if len(digits) < 2:
            return -1
        
        digits = sorted(digits)
        return digits[-2]

print(Solution().secondHighest("dfa12321afd"))