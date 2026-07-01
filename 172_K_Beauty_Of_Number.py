class Solution(object):
    def divisorSubstrings(self, num, k):
        s = str(num)
        count = 0 
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if len(s[i:j]) == k : 
                    sub = int(s[i:j])
                    if sub != 0 and num % sub == 0 : 
                        count+=1
        return count
    
print(Solution().divisorSubstrings(430043, 2)) 