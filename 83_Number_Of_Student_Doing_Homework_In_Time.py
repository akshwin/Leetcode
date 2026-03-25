class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count+=1
        return count

print(Solution().busyStudent([1,2,3], [3,2,7], 4)) # 1