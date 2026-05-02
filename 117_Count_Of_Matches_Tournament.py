class Solution(object):
    def numberOfMatches(self, n):
        played = 0 
        while n>1:
            if n %2 == 0 : 
                played +=n//2
                n = n//2
            else:
                played+=(n-1)//2
                n = (n-1)//2+1
        return played
                
print(Solution().numberOfMatches(7))  # Output: 6