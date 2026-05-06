class Solution(object):
    def sortPeople(self, names, heights):
        return [name for _,name in sorted(zip(heights,names),reverse=True)]

print(Solution().sortPeople(["Mary","John","Emma"], [180,165,170]))