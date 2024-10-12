import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        targetArrival = times[targetFriend][0]

        openpq = []
        sitpq = []
        nextSeat = 0

        times.sort()

        for start, end in times:

            while sitpq and sitpq[0][0] <= start: 
                heapq.heappush(openpq, sitpq[0][1])
                heapq.heappop(sitpq)

            seat = None
            if openpq:
                seat = openpq[0]
                heapq.heappop(openpq)
            else: 
                seat = nextSeat
                nextSeat += 1
            
            if start == targetArrival: 
                return seat
            
            heapq.heappush(sitpq, (end, seat))
            
            
        return -5

