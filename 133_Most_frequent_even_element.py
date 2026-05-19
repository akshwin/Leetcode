from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        count = Counter()

        for num in nums:
            if num%2 == 0 :
                count[num] +=1
        
        if not count:
            return -1

        ans = -1 
        freq = 0 

        for num,c in count.items():
            if c>freq or (c == freq and num<ans):
                freq = c
                ans = num
        return ans

print(Solution().mostFrequentEven([0,1,2,2,4,4,1]))