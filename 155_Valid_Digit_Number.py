class Solution(object):
    def validDigit(self, n, x):
        n_string = str(n)
        x = str(x)

        return x in n_string[1:] and n_string[0] != x

print(Solution().validDigit(123, 1))  # True