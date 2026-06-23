class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()

        moves = 0 
        for s , st in zip(seats,students):
            moves+=abs(s-st)
        
        return moves

print(Solution().minMovesToSeat([3,1,5], [2,7,4])) # Output: 4