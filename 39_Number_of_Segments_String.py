class Solution(object):
    def countSegments(self, s):
        split = s.split()
        return len(split)

print(Solution().countSegments("Hello, my name is John"))