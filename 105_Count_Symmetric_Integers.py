class Solution(object):
    def countSymmetricIntegers(self, low, high):
        count = 0 
        for num in range(low, high + 1):
            s = str(num)
            n = len(s)
            
            if n % 2 != 0:
                continue
                
            half = n // 2
            left_sum = sum(int(d) for d in s[:half])
            right_sum = sum(int(d) for d in s[half:])
            
            if left_sum == right_sum:
                count += 1
                
        return count

print(Solution().countSymmetricIntegers(1, 100))