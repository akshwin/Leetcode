class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x:x[1], reverse=True)

        total_units = 0 

        for boxes , units in boxTypes:
            take = min(truckSize,boxes)
            total_units += take * units
            truckSize -= take

            if truckSize == 0 : 
                break 
            
        return total_units

print(Solution().maximumUnits([[1,3],[2,2],[3,1]], 4)) # Output: 8