class Solution(object):
    def halvesAreAlike(self, s):
        mid = len(s)//2
        vowels = "aeiouAEIOU"
        count1 = 0
        count2 = 0 

        for i in range(0,mid):
            if s[i] in vowels:
                count1+=1
        for i in range(mid,len(s)):
            if s[i] in vowels:
                count2+=1
        if count1== count2:
            return True
        return False

print(Solution().halvesAreAlike("book"))