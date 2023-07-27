class Solution:
    # We need k closest points
    # The best way I could do this is with a priority queue
    # And also then to not square root cuz that is unncecssary
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Creating a minheap with points
        minHeap = [(point[0] * point[0] + point[1] * point[1], point[0], point[1]) for point in points]
        heapq.heapify(minHeap)

        print(minHeap)

        minHeap = heapq.nsmallest(k, minHeap)

        return [[item[1], item[2]] for item in minHeap]