class Solution(object):
    def areNumbersAscending(self, s):
        arr = []
        
        for i in s.split() : 
            if i.isnumeric():
                arr.append(int(i))
                
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True

print(Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))