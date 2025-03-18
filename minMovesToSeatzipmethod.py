class Solution(object):
    def minMovesToSeat(self,seats, students):
        seats.sort()
        students.sort()

        return sum(abs(s - st) for s, st in zip(seats, students)) 