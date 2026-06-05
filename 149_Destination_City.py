class Solution(object):
    def destCity(self, paths):
        starts = {a for a,b in paths}

        for a , b in paths:
            if b not in starts:
                return b

print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))