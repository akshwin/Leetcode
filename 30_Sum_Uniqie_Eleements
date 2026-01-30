class Solution(object):
    def sumOfUnique(self, nums):
        sum = 0 
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1

        for key in freq:
            if freq[key] == 1:
                sum+=key
        return sum    

print(Solution().sumOfUnique([1,2,3,2]))  # Output: 4