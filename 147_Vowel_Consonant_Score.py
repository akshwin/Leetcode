class Solution(object):
    def vowelConsonantScore(self, s):
        vow_count = 0 
        const_count = 0 
        vowels = 'aeiou'
        for i in s : 
            if i.isalpha():
                if i in vowels:
                    vow_count+=1
                else:
                    const_count+=1

        if const_count == 0 : 
            return 0 

        return vow_count//const_count
        
print(Solution().vowelConsonantScore("aeiou")) # 0